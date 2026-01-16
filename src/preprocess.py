import re

SKILL_NORMALIZATION_MAP = {
    "ml": "machine learning",
    "machine-learning": "machine learning",
    "dl": "deep learning",
    "ai": "artificial intelligence"
}


def clean_text(text: str) -> str:

    #Lowercases text and removes punctuation.

    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", "", text)
    return text.strip()


def normalize_skill(skill: str) -> str:
    
    #Normalizes skill names using predefined mappings.
    
    skill = clean_text(skill)

    if skill in SKILL_NORMALIZATION_MAP:
        return SKILL_NORMALIZATION_MAP[skill]

    return skill


def preprocess_skill_list(skills: list) -> list:
    
    #Applies cleaning and normalization to a list of skills.
    
    normalized_skills = []

    for skill in skills:
        normalized_skill = normalize_skill(skill)
        normalized_skills.append(normalized_skill)

    return normalized_skills
