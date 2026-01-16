from src.scorer import calculate_final_score

score = calculate_final_score(
    match_ratio=0.8,
    has_relevant_experience=True,
    is_education_relevant=True
)

print(score)
