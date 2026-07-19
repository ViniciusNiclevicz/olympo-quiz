import random
from collections import defaultdict


def stratified_sample(question_bank, total=50, min_per_trait=2):
    """
    Sorteia um subconjunto de perguntas do banco, garantindo que
    cada traço apareça pelo menos `min_per_trait` vezes (quando o
    banco tiver perguntas suficientes daquele traço), e completa o
    restante com um sorteio aleatório entre as perguntas que sobraram.

    Isso evita que, num sorteio totalmente aleatório, algum traço
    fique sem nenhuma pergunta e distorça o cálculo do perfil.
    """

    by_trait = defaultdict(list)
    for question in question_bank:
        by_trait[question["primary_trait"]].append(question)

    selected = []
    selected_ids = set()

    # 1) garante cobertura mínima por traço
    for trait, items in by_trait.items():
        pool = items[:]
        random.shuffle(pool)
        take = pool[:min_per_trait]

        for question in take:
            if question["id"] not in selected_ids:
                selected.append(question)
                selected_ids.add(question["id"])

    # 2) completa o restante aleatoriamente entre as perguntas não usadas
    remaining_pool = [
        q for q in question_bank
        if q["id"] not in selected_ids
    ]
    random.shuffle(remaining_pool)

    missing = max(0, total - len(selected))
    selected.extend(remaining_pool[:missing])

    # 3) se por acaso passou do total (banco pequeno / min_per_trait alto),
    # corta aleatoriamente mantendo a cobertura mínima já garantida
    if len(selected) > total:
        selected = selected[:total]

    random.shuffle(selected)

    return selected
