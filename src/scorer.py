# Scoring weights (hardcoded)
SKILL_WEIGHT = 60
EXPERIENCE_WEIGHT = 25
EDUCATION_WEIGHT = 15


def calculate_skill_score(match_ratio: float) -> float:
    
    #Calculates skill score based on match ratio
    
    return match_ratio * SKILL_WEIGHT


def calculate_experience_score(has_relevant_experience: bool) -> float:
    
    #Calculates experience score.
    
    if has_relevant_experience:
        return EXPERIENCE_WEIGHT
    return 0.0


def calculate_education_score(is_education_relevant: bool) -> float:
    
    #Calculates education score.
    
    if is_education_relevant:
        return EDUCATION_WEIGHT
    return 0.0


def calculate_final_score(
    match_ratio: float,
    has_relevant_experience: bool,
    is_education_relevant: bool
) -> float:
    
    #Combines all components into a final JD match score.
    
    skill_score = calculate_skill_score(match_ratio)
    experience_score = calculate_experience_score(has_relevant_experience)
    education_score = calculate_education_score(is_education_relevant)

    final_score = skill_score + experience_score + education_score

    # Clamp score between 0 and 100
    return round(min(final_score, 100.0), 2)
