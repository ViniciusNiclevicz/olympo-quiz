from math import sqrt


def cosine_similarity(user, god):
    dot_product = 0
    user_norm = 0
    god_norm = 0

    for trait in god.keys():
        user_value = user.get(trait, 0)
        god_value = god.get(trait, 0)

        dot_product += user_value * god_value
        user_norm += user_value ** 2
        god_norm += god_value ** 2

    if user_norm == 0 or god_norm == 0:
        return 0

    return dot_product / (sqrt(user_norm) * sqrt(god_norm))


def rank_gods(user_profile, gods):
    ranking = []

    for god_name, god_profile in gods.items():
        similarity = cosine_similarity(user_profile, god_profile)

        ranking.append({
            "god": god_name,
            "score": similarity
        })

    ranking.sort(key=lambda x: x["score"], reverse=True)

    return ranking


def calculate_percentages(ranking):
    if not ranking:
        return ranking

    # aumenta contraste entre perfis parecidos
    powered_scores = [
        item["score"] ** 15
        for item in ranking
    ]

    total = sum(powered_scores)

    for item, score in zip(ranking, powered_scores):
        item["percentage"] = round(
            (score / total) * 100,
            2
        )

    return ranking