def calculate_match_score(candidate_skills, jd_skills):

    if not jd_skills:
        return 0

    candidate_skills = set([
        skill.lower().strip()
        for skill in candidate_skills
    ])

    jd_skills = set([
        skill.lower().strip()
        for skill in jd_skills
    ])

    matched_skills = candidate_skills.intersection(jd_skills)

    match_ratio = len(matched_skills) / len(jd_skills)

    skill_score = match_ratio * 100

    return round(skill_score, 2)