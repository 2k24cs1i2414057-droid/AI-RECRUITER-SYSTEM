import streamlit as st
import pandas as pd
import plotly.express as px
import re

from modules.parser import parse_resume
from modules.matcher import calculate_match_score
from modules.semantic_matcher import semantic_score
from modules.skill_gap import get_missing_skills
from modules.ranking import rank_candidates
from modules.explainable_score import explain_score
from modules.roadmap import generate_roadmap


SKILL_KEYWORDS = {
    "python": ["python"],
    "django": ["django"],
    "flask": ["flask"],
    "streamlit": ["streamlit"],
    "fastapi": ["fastapi"],
    "rest api": ["rest api", "rest apis", "api", "apis"],

    "sql": ["sql", "mysql", "sqlite", "postgresql"],
    "mysql": ["mysql"],
    "sqlite": ["sqlite"],
    "mongodb": ["mongodb", "mongo db"],
    "postgresql": ["postgresql", "postgres"],

    "git": ["git"],
    "github": ["github"],
    "html": ["html"],
    "css": ["css"],
    "javascript": ["javascript", "js"],
    "react": ["react", "react.js", "reactjs"],
    "firebase": ["firebase"],

    "pandas": ["pandas"],
    "numpy": ["numpy"],
    "matplotlib": ["matplotlib"],
    "seaborn": ["seaborn"],
    "scikit-learn": ["scikit-learn", "sklearn", "scikit learn"],

    "machine learning": ["machine learning", "ml"],
    "deep learning": ["deep learning", "dl"],
    "artificial intelligence": ["artificial intelligence", "ai"],
    "data science": ["data science"],
    "data analysis": ["data analysis", "data analytics"],
    "eda": ["eda", "exploratory data analysis"],
    "data cleaning": ["data cleaning", "data preprocessing"],
    "feature engineering": ["feature engineering"],
    "model evaluation": ["model evaluation"],
    "predictive analytics": ["predictive analytics"],

    "linear regression": ["linear regression"],
    "logistic regression": ["logistic regression"],
    "decision tree": ["decision tree"],
    "random forest": ["random forest"],
    "knn": ["knn", "k-nearest neighbors"],
    "k-means": ["k-means", "kmeans"],
    "dbscan": ["dbscan"],
    "svm": ["svm", "support vector machine"],
    "ann": ["ann", "artificial neural network"],
    "cnn": ["cnn", "convolutional neural network"],
    "nlp": ["nlp", "natural language processing"],

    "generative ai": ["generative ai", "genai"],
    "llm": ["llm", "large language model"],
    "rag": ["rag", "retrieval augmented generation"],
    "prompt engineering": ["prompt engineering"],

    "excel": ["excel", "ms excel"],
    "power bi": ["power bi", "powerbi"],
    "tableau": ["tableau"],
    "statistics": ["statistics", "statistical analysis"],
    "visualization": ["visualization", "data visualization"],

    "aws": ["aws", "amazon web services"],
    "azure": ["azure"],
    "gcp": ["gcp", "google cloud"],
    "docker": ["docker"],
    "kubernetes": ["kubernetes", "k8s"],
    "linux": ["linux"],
    "jenkins": ["jenkins"],
    "ci/cd": ["ci/cd", "cicd"],

    "oop": ["oop", "oops", "object oriented programming"],
    "dsa": ["dsa", "data structures", "algorithms"],
    "problem solving": ["problem solving"],
    "debugging": ["debugging"]
}


def remove_bias_info(text):
    text = re.sub(r'\S+@\S+', ' ', text)
    text = re.sub(r'\+?\d[\d\s-]{8,}\d', ' ', text)
    text = re.sub(
        r'\b(male|female|gender|dob|date of birth|age|married|single)\b',
        ' ',
        text,
        flags=re.IGNORECASE
    )
    return text


def extract_jd_skills(jd_text):
    jd_text = jd_text.lower()
    jd_skills = []

    for skill, aliases in SKILL_KEYWORDS.items():
        for alias in aliases:
            pattern = r'\b' + re.escape(alias.lower()) + r'\b'
            if re.search(pattern, jd_text):
                jd_skills.append(skill)
                break

    return sorted(list(set(jd_skills)))


st.set_page_config(
    page_title="AI Recruiter System",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Recruiter System")

st.markdown(
    "Hybrid AI Resume Screening System Using Skill Matching And SentenceTransformer Semantic Matching."
)

st.sidebar.header("Project Info")
st.sidebar.info(
    """
Features:
✔ Resume Parsing
✔ JD Skill Extraction
✔ Skill Match Score
✔ SentenceTransformer Semantic Score
✔ Bias-Free Hiring
✔ Candidate Ranking
✔ Skill Gap Analysis
✔ Learning Roadmap
✔ CSV Export
"""
)

st.subheader("Job Description")

jd_text = st.text_area(
    "Paste Job Description Here",
    height=250
)

st.subheader("Upload Resumes")

uploaded_files = st.file_uploader(
    "Upload PDF Resumes",
    type=["pdf"],
    accept_multiple_files=True
)

if st.button("🚀 Analyze Candidates"):

    if not jd_text.strip():
        st.error("Please enter a Job Description.")
        st.stop()

    if not uploaded_files:
        st.error("Please upload at least one resume.")
        st.stop()

    with st.spinner("Analyzing resumes..."):

        jd_skills = extract_jd_skills(jd_text)

        st.subheader("Skills Found in JD")

        if jd_skills:
            st.success(", ".join(jd_skills))
        else:
            st.warning("No clear technical skills found in JD.")

        candidates = []
        progress_bar = st.progress(0)

        for index, file in enumerate(uploaded_files):

            try:
                resume_data = parse_resume(file)

                resume_skills = [
                    skill.lower().strip()
                    for skill in resume_data["skills"]
                ]

                skill_score = calculate_match_score(
                    resume_skills,
                    jd_skills
                )

                bias_free_text = remove_bias_info(
                    resume_data["text"]
                )

                semantic_match = semantic_score(
                    jd_text,
                    bias_free_text
                )

                score_data = explain_score(
                    skill_score,
                    semantic_match
                )

                final_score = score_data["final_score"]

                missing_skills = get_missing_skills(
                    resume_skills,
                    jd_skills
                )

                status = (
                    "Highly Recommended" if final_score >= 75
                    else "Recommended" if final_score >= 60
                    else "Consider" if final_score >= 45
                    else "Not Recommended"
                )

                candidates.append({
                    "Candidate": file.name,
                    "Email": resume_data["email"],
                    "Phone": resume_data["phone"],
                    "Resume Skills": ", ".join(resume_skills),
                    "JD Skills": ", ".join(jd_skills),
                    "Skill Score": skill_score,
                    "Semantic Score": semantic_match,
                    "ATS Compatibility Score": final_score,
                    "Status": status,
                    "Missing Skills": ", ".join(missing_skills)
                })

                progress_bar.progress((index + 1) / len(uploaded_files))

            except Exception as e:
                st.error(f"Error processing {file.name}: {e}")

        if candidates:

            ranked_df = rank_candidates(candidates)

            st.success("Analysis Completed Successfully!")

            st.subheader("🏆 Candidate Ranking")

            st.info(
                "⚖️ Bias-Free Hiring Enabled: Personal identifiers are removed before semantic matching."
            )

            top_candidate = ranked_df.iloc[0]

            st.success(
                f"🏆 Best Candidate: {top_candidate['Candidate']} | "
                f"ATS Score: {top_candidate['ATS Compatibility Score']}% | "
                f"Status: {top_candidate['Status']}"
            )

            display_df = ranked_df[
                [
                    "Rank",
                    "Candidate",
                    "ATS Compatibility Score",
                    "Skill Score",
                    "Semantic Score",
                    "Status",
                    "Missing Skills"
                ]
            ]

            st.dataframe(
                display_df,
                use_container_width=True,
                hide_index=True
            )

            csv = ranked_df.to_csv(index=False)

            st.download_button(
                label="📥 Download Full Ranking CSV",
                data=csv,
                file_name="candidate_ranking.csv",
                mime="text/csv"
            )

            st.subheader("Candidate Analysis")

            for _, row in ranked_df.iterrows():

                with st.expander(
                    f"{row['Candidate']} | ATS Score: {row['ATS Compatibility Score']}% | {row['Status']}"
                ):

                    st.write(f"**Email:** {row['Email']}")
                    st.write(f"**Phone:** {row['Phone']}")
                    st.write(f"**Resume Skills:** {row['Resume Skills']}")
                    st.write(f"**JD Skills:** {row['JD Skills']}")
                    st.write(f"**Skill Score:** {row['Skill Score']}%")
                    st.write(f"**Semantic Score:** {row['Semantic Score']}%")
                    st.write(f"**Missing Skills:** {row['Missing Skills']}")
                    st.write(f"**Recommendation Status:** {row['Status']}")

                    chart_df = pd.DataFrame({
                        "Category": ["Skill Match", "Semantic Match"],
                        "Score": [row["Skill Score"], row["Semantic Score"]]
                    })

                    fig = px.pie(
                        chart_df,
                        names="Category",
                        values="Score",
                        title="Explainable AI Score Breakdown"
                    )

                    st.plotly_chart(fig, use_container_width=True)

                    if row["Missing Skills"]:

                        st.subheader("📚 Skill Gap Roadmap")

                        roadmap = generate_roadmap(
                            row["Missing Skills"].split(", ")
                        )

                        for step in roadmap:
                            st.write(f"✅ {step}")

        else:
            st.warning("No valid resumes could be processed.")

