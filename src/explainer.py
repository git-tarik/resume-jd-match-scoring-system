def generate_explanation(
    matched_skills: set,
    missing_skills: set,
    total_required_skills: int,
    has_relevant_experience: bool,
    is_education_relevant: bool
) -> str:
    
    #Generates a rule-based explanation for the JD match score.
    

    explanation_lines = []

    # Skill match explanation
    matched_count = len(matched_skills)
    explanation_lines.append(
        f"Matched {matched_count} out of {total_required_skills} required skills "
        f"({', '.join(sorted(matched_skills))})."
    )

    # Experience explanation
    if has_relevant_experience:
        explanation_lines.append(
            "Relevant internship or project experience contributes positively to the score."
        )
    else:
        explanation_lines.append(
            "Lack of relevant hands-on experience reduces the overall match score."
        )

    # Education explanation
    if is_education_relevant:
        explanation_lines.append(
            "Educational background aligns with the job requirements."
        )
    else:
        explanation_lines.append(
            "Educational background does not fully align with the job requirements."
        )

    # Missing skills explanation
    if missing_skills:
        explanation_lines.append(
            f"Missing required skills include: {', '.join(sorted(missing_skills))}."
        )
    else:
        explanation_lines.append(
            "No major skill gaps were identified for this role."
        )

    return "\n".join(explanation_lines)
