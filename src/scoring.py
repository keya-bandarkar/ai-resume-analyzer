def compute_skill_match_ratio(resume_skills: set[str], jd_skills: set[str]) -> float:
    if not jd_skills:
        return 0.0
    return len(resume_skills & jd_skills) / len(jd_skills)

def compute_keyword_score(resume_text: str, jd_text: str) -> float:
    """
    Simple keyword heuristic: if role name appears in resume, give a boost.
    You can extend this with more patterns.
    """
    role_keywords = ["data scientist", "machine learning engineer",
                     "data analyst", "ai engineer"]
    found = any(k in resume_text for k in role_keywords)
    return 1.0 if found else 0.0

def compute_final_score(skill_match_ratio: float,
                        keyword_score: float) -> float:
    """
    Combine into a 0–100 score.
    Skill match plays major role, role keywords give a small boost.
    """
    score = 0.8 * skill_match_ratio + 0.2 * keyword_score
    return round(score * 100, 1)
