import json

from src.preprocess import preprocess_skill_list
from src.matcher import (
    get_skill_sets,
    find_matched_skills,
    find_missing_skills,
    calculate_match_ratio
)
from src.scorer import calculate_final_score
from src.explainer import generate_explanation


def load_json(file_path: str) -> dict:
    with open(file_path, "r") as file:
        return json.load(file)


def main():
    # Load input data
    student_profile = load_json("data/student_profile.json")
    job_description = load_json("data/job_description.json")

    # Preprocess skills
    student_skills = preprocess_skill_list(student_profile.get("skills", []))
    job_required_skills = preprocess_skill_list(job_description.get("required_skills", []))


    # Matching logic
    student_set, job_set = get_skill_sets(student_skills, job_required_skills)
    matched_skills = find_matched_skills(student_set, job_set)
    missing_skills = find_missing_skills(student_set, job_set)
    match_ratio = calculate_match_ratio(matched_skills, len(job_set),len(student_set))

    # Experience relevance (simple keyword-based logic)
    has_relevant_experience = any(
      any(
          keyword in exp.get("domain", "").lower()
          for keyword in ["machine learning", "ml", "data"]
      )
      for exp in student_profile.get("experience", [])
    )

    # Education relevance (simple check)
    education_branch = student_profile.get("education", {}).get("branch", "")
    is_education_relevant = "computer" in education_branch.lower()

    # Scoring
    final_score = calculate_final_score(
        match_ratio,
        has_relevant_experience,
        is_education_relevant
    )

    # Explanation
    explanation = generate_explanation(
        matched_skills,
        missing_skills,
        len(job_set),
        has_relevant_experience,
        is_education_relevant
    )

    # Output
    print(f"\nJD Match Score: {final_score}%\n")
    print("Explanation:")
    print(explanation)


if __name__ == "__main__":
    main()
