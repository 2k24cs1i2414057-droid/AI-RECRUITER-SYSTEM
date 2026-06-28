def explain_score(skill_score, semantic_score):

    final_score = (
        skill_score * 0.4 +
        semantic_score * 0.6
    )

    if final_score > 100:
        final_score = 100

    return {
        "skill_score": skill_score,
        "semantic_score": semantic_score,
        "final_score": round(final_score, 2)
    }