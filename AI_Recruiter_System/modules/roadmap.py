def generate_roadmap(missing_skills):

    roadmap = []

    for skill in missing_skills:

        roadmap.append(
            f"Learn {skill} basics from documentation or beginner tutorials."
        )

        roadmap.append(
            f"Practice {skill} with 2-3 small hands-on examples."
        )

        roadmap.append(
            f"Build one mini project using {skill}."
        )

    return roadmap