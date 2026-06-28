from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


model = SentenceTransformer("all-MiniLM-L6-v2")


def semantic_score(jd_text, resume_text):

    if not jd_text.strip() or not resume_text.strip():
        return 0

    jd_embedding = model.encode(jd_text)
    resume_embedding = model.encode(resume_text)

    similarity = cosine_similarity(
        [jd_embedding],
        [resume_embedding]
    )[0][0]

    score = similarity * 100

    return round(score, 2)
