def get_missing_skills(candidate_skills, jd_skills):

    candidate_skills = set([
        skill.lower().strip()
        for skill in candidate_skills
    ])

    jd_skills = set([
        skill.lower().strip()
        for skill in jd_skills
    ])

    missing = jd_skills - candidate_skills

    return sorted(list(missing))