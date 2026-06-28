# 🤖 AI Recruiter System

An **AI-powered Resume Screening and Candidate Ranking System** that automates the recruitment process by analyzing resumes against job descriptions using **Hybrid ATS Scoring** and **Semantic AI Matching**.

---

## 📌 Problem Statement

Recruiters spend significant time manually screening resumes, which leads to delays, inconsistent evaluations, and increased hiring costs. This project automates the recruitment screening process by analyzing resumes against job descriptions and ranking candidates based on skill matching and semantic relevance.

---

## 🚀 Features

* PDF Resume Parsing
* Job Description Skill Extraction
* Hybrid ATS Score Calculation
* Semantic Resume-JD Matching
* Candidate Ranking
* Skill Gap Analysis
* Learning Roadmap Generation
* Explainable AI Score Breakdown
* Interactive Dashboard
* CSV Export of Ranked Candidates

---

## 🧠 AI Approach

The system uses a **Hybrid Evaluation Strategy** combining traditional ATS scoring with semantic understanding.

### Skill Matching (40%)

* Regex-based skill extraction
* Keyword matching between resume and job description
* Missing skill identification

### Semantic Matching (60%)

* Sentence embeddings generated using SentenceTransformer
* Model: `all-MiniLM-L6-v2`
* Contextual similarity measurement between resumes and job descriptions

### Final ATS Score Formula

```text
ATS Score = (Skill Score × 0.4) + (Semantic Score × 0.6)
```

---

## 🎯 Candidate Classification

| ATS Score | Recommendation     |
| --------- | ------------------ |
| 85–100    | Highly Recommended |
| 70–84     | Recommended        |
| 50–69     | Consider           |
| Below 50  | Not Recommended    |

---

## 🛠️ Tech Stack

* Python
* Streamlit
* pdfplumber
* Sentence Transformers
* Scikit-learn
* Pandas
* Plotly
* python-dotenv

---

## 📂 Project Structure

```bash
AI-RECRUITER-SYSTEM/
│
├── app.py
├── parser.py
├── matcher.py
├── semantic_matcher.py
├── ranking.py
├── explainable_score.py
├── requirements.txt
├── README.md
│
└── modules/
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/2k24cs1i2414057-droid/AI-RECRUITER-SYSTEM.git

cd AI-RECRUITER-SYSTEM
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
streamlit run app.py
```

---

## 📊 Workflow

```text
Job Description Input
          ↓
Resume Upload (PDF)
          ↓
Resume Parsing
          ↓
Skill Extraction
          ↓
Semantic Matching
          ↓
ATS Score Calculation
          ↓
Candidate Ranking
          ↓
Skill Gap Analysis
          ↓
Learning Roadmap Generation
          ↓
Export Results
```

---

## 📈 Output

The system provides:

* ATS Score
* Skill Match Score
* Semantic Similarity Score
* Candidate Ranking
* Missing Skills Analysis
* Personalized Learning Roadmap
* Explainable AI Visualizations
* CSV Export of Results

---

## 📊 Dashboard Features

* Candidate Ranking Leaderboard
* ATS Score Visualization
* Skill Match Analysis
* Semantic Similarity Scores
* Explainable AI Pie Charts
* Missing Skills Report
* Exportable CSV Reports

---

## 🔮 Future Enhancements

* LinkedIn Profile Integration
* AI-Based Resume Feedback
* Voice-Based Interview Analysis
* Multi-language Resume Support
* AI Interview Question Generation
* Recruiter Analytics Dashboard
* Resume Recommendation Engine

---

## 🏆 Project Objective

The primary objective of this project is to simplify and automate the candidate screening process by combining traditional ATS mechanisms with semantic artificial intelligence techniques. The system aims to reduce recruiter workload, improve candidate selection accuracy, and provide transparent and explainable hiring recommendations.

---

## 📄 License

This project was developed for educational, research, and demonstration purposes only.

---

## ⭐ Support

If you found this project useful, consider giving the repository a ⭐ on GitHub.

---

**Made with ❤️ using Artificial Intelligence and Machine Learning**
