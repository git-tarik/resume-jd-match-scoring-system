def get_skill_sets(student_skills: list, job_required_skills: list):
    
    #Converts skill lists to sets
    
    return set(student_skills), set(job_required_skills)


def find_matched_skills(student_skills: set, job_required_skills: set) -> set:
    
    #Finds skills present in both student profile and job description
    
    return student_skills.intersection(job_required_skills)


def find_missing_skills(student_skills: set, job_required_skills: set) -> set:
    
    #Finds required skills missing from the student profile
    
    return job_required_skills.difference(student_skills)


def calculate_match_ratio(matched_skills: set, total_required_skills: int, total_student_skills: int) -> float:
    
    #Calculates ratio of matched skills
    
    if total_required_skills == 0 or total_student_skills == 0:
        return 0.0

    return len(matched_skills) / total_required_skills
