import pdfplumber
import re


SKILLS_DB = {
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


def extract_text(pdf_file):
    text = ""

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    return text


def extract_email(text):
    match = re.search(r'[\w\.-]+@[\w\.-]+', text)
    return match.group(0) if match else "Not Found"


def extract_phone(text):
    match = re.search(r'\+?\d[\d\s-]{8,15}', text)
    return match.group(0) if match else "Not Found"


def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9+#./\s-]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def extract_skills(text):
    text = clean_text(text)
    skills = []

    for skill, aliases in SKILLS_DB.items():
        for alias in aliases:
            pattern = r'\b' + re.escape(alias.lower()) + r'\b'
            if re.search(pattern, text):
                skills.append(skill)
                break

    return sorted(list(set(skills)))


def parse_resume(pdf_file):
    text = extract_text(pdf_file)

    return {
        "email": extract_email(text),
        "phone": extract_phone(text),
        "skills": extract_skills(text),
        "text": clean_text(text)
    }