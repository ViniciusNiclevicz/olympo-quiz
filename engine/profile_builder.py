from collections import defaultdict


def build_user_profile(answers, questions):
    """
    Constrói o perfil de traços do usuário a partir das respostas
    em escala Likert (1 a 7, onde 4 = neutro).

    answers: lista de dicts {"question_id": int, "value": int (1-7)}
    questions: lista de perguntas do banco (cada uma com "weights",
               um dict trait -> coeficiente, que pode ser negativo
               para itens invertidos).

    Cada traço é normalizado para uma escala de 0 a 10, na mesma
    escala usada no perfil das divindades (data/gods.json), o que
    torna a similaridade de cosseno entre os vetores comparável.
    """

    questions_by_id = {q["id"]: q for q in questions}

    raw_totals = defaultdict(float)
    abs_weight_sums = defaultdict(float)

    for answer in answers:

        question = questions_by_id.get(answer["question_id"])

        if question is None:
            continue

        value = answer.get("value")

        if value is None:
            continue

        try:
            value = int(value)
        except (TypeError, ValueError):
            continue

        # trava a resposta na escala válida (1 a 7)
        value = max(1, min(7, value))

        # centraliza em torno do neutro (4) -> intervalo -3 a +3
        centered = value - 4

        for trait, weight in question.get("weights", {}).items():
            raw_totals[trait] += centered * weight
            abs_weight_sums[trait] += abs(weight)

    profile = {}

    for trait, abs_sum in abs_weight_sums.items():

        if abs_sum == 0:
            continue

        # normaliza de [-3*abs_sum, +3*abs_sum] para [0, 10]
        normalized = (
            (raw_totals[trait] + 3 * abs_sum) / (6 * abs_sum)
        ) * 10

        profile[trait] = round(normalized, 2)

    return profile
