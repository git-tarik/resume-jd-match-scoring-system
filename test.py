from src.matcher import (
    get_skill_sets,
    find_matched_skills,
    find_missing_skills,
    calculate_match_ratio
)

student = ["python", "machine learning", "sql"]
job = ["python", "machine learning", "nlp"]

student_set, job_set = get_skill_sets(student, job)

matched = find_matched_skills(student_set, job_set)
missing = find_missing_skills(student_set, job_set)
ratio = calculate_match_ratio(matched, len(job_set))

print("Matched:", matched)
print("Missing:", missing)
print("Match ratio:", ratio)
