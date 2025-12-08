import os

from config import RESUME_DIR, JD_DIR, SKILL_FILE
from text_extraction import extract_text
from preprocessing import clean_text
from skills_matching import load_skills, extract_present_skills
from scoring import compute_skill_match_ratio, compute_keyword_score, compute_final_score


def analyze_resume(resume_filename: str, jd_filename: str):
    # Paths
    resume_path = os.path.join(RESUME_DIR, resume_filename)
    jd_path = os.path.join(JD_DIR, jd_filename)

    # Load skills
    all_skills = load_skills(SKILL_FILE)

    # Extract + clean text
    resume_raw = extract_text(resume_path)
    jd_raw = extract_text(jd_path)

    resume_text = clean_text(resume_raw)
    jd_text = clean_text(jd_raw)

    # Extract skills
    resume_skills = set(extract_present_skills(resume_text, all_skills))
    jd_skills = set(extract_present_skills(jd_text, all_skills))

    # Compute metrics
    skill_match_ratio = compute_skill_match_ratio(resume_skills, jd_skills)
    keyword_score = compute_keyword_score(resume_text, jd_text)
    final_score = compute_final_score(skill_match_ratio, keyword_score)

    missing_skills = jd_skills - resume_skills

    # Print results
    print("=== AI Resume Analyzer ===")
    print(f"Resume file: {resume_filename}")
    print(f"Job description file: {jd_filename}\n")

    print(f"Skills required in JD: {sorted(jd_skills) if jd_skills else 'None detected'}")
    print(f"Skills found in resume: {sorted(resume_skills) if resume_skills else 'None detected'}")
    print(f"Missing skills: {sorted(missing_skills) if missing_skills else 'None'}\n")

    print(f"Skill match ratio: {round(skill_match_ratio * 100, 1)}%")
    print(f"Final ATS-style score: {final_score}/100\n")


if __name__ == "__main__":
    # You can change these filenames or take them from input()
    analyze_resume("sample_resume.txt", "sample_jd.txt")
