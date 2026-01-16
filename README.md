# JD Match Scoring System

## Problem Statement
The goal of this project is to design a simple and explainable system that evaluates how well a student’s CV/profile matches a given job description.  
The system takes one student profile and one job description as input and outputs:
- a JD match score (0–100)
- a brief, human-readable explanation justifying the score

The focus is on analytical reasoning, transparency, and logic rather than complex machine learning models.

---

## Approach Overview
The system is implemented as a modular Python pipeline consisting of the following stages:

1. **Preprocessing**
   - Normalize skill text by lowercasing and removing punctuation
   - Map common abbreviations (e.g., "ml" → "machine learning")

2. **Matching**
   - Convert student skills and job-required skills into sets
   - Identify matched skills and missing required skills
   - Compute a skill match ratio

3. **Scoring**
   - Assign weighted scores to skills, experience, and education
   - Combine these components into a final JD match score

4. **Explanation Generation**
   - Generate a deterministic, rule-based explanation
   - Clearly state matched skills, missing skills, and relevance of experience and education

The system is fully deterministic and does not rely on external APIs or black-box models.

---

## Scoring Methodology
The final JD match score is calculated using fixed weights:

- **Skill Match (60%)**
  - Based on the ratio of matched required skills to total required skills

- **Experience Relevance (25%)**
  - Full score awarded if the student has relevant internship or project experience

- **Education Alignment (15%)**
  - Full score awarded if the educational background aligns with the job domain

Final Score = Skill Score + Experience Score + Education Score  
The score is capped at 100.

---

## Explanation Logic
The explanation is generated using rule-based logic derived from computed facts. It includes:
- Number of matched skills out of total required skills
- Contribution of relevant experience (if present)
- Alignment of educational background
- List of missing required skills (if any)

Each explanation directly reflects the scoring logic, ensuring transparency and interpretability.

---

## Assumptions
- Skills are provided as keyword lists
- All required skills are treated with equal importance
- Experience relevance is determined using keyword-based matching
- Education relevance is checked using simple domain alignment
- The system processes one student profile and one job description at a time

---

## Future Extensions
- Support for evaluating multiple candidates or job descriptions in batch
- Use of NLP techniques such as TF-IDF or embeddings for semantic skill matching
- Integration as a REST API and optional web interface
- Enhanced experience relevance scoring using project descriptions
