import gradio as gr

# Example skills list – you can extend this
MASTER_SKILLS = [
    "python", "sql", "machine learning", "deep learning",
    "nlp", "flask", "fastapi", "django",
    "pandas", "numpy", "scikit-learn",
    "tensorflow", "pytorch",
    "power bi", "tableau",
    "git", "docker",
]


def analyze_resume(jd_text: str, resume_text: str):
    if not jd_text.strip() or not resume_text.strip():
        return (
            [],
            [],
            0.0,
            0.0,
            "Please provide both job description and resume text.",
        )

    jd_lower = jd_text.lower()
    resume_lower = resume_text.lower()

    # Skills required (present in JD)
    jd_skills = [s for s in MASTER_SKILLS if s in jd_lower]

    # Skills present in resume
    resume_skills = [s for s in MASTER_SKILLS if s in resume_lower]

    # Intersection and missing
    matched = sorted(list(set(jd_skills) & set(resume_skills)))
    missing = sorted(list(set(jd_skills) - set(resume_skills)))

    if jd_skills:
        skill_match_ratio = len(matched) / len(set(jd_skills))
    else:
        skill_match_ratio = 0.0

    skill_match_percent = round(skill_match_ratio * 100, 2)

    # Simple ATS-style score: 60% from skills + 40% from keyword density
    # (very simple heuristic)
    keyword_hits = sum(resume_lower.count(skill) for skill in matched)
    keyword_score = min(keyword_hits * 5, 40)  # cap at 40

    final_score = round((skill_match_percent * 0.6) + keyword_score, 2)

    summary = (
        f"Skills required in JD: {jd_skills}\n"
        f"Skills found in resume: {resume_skills}\n"
        f"Matched skills: {matched}\n"
        f"Missing skills: {missing}\n"
        f"Skill match: {skill_match_percent}%\n"
        f"Final ATS-style score: {final_score}/100"
    )

    return matched, missing, skill_match_percent, final_score, summary


with gr.Blocks(title="AI Resume Analyzer") as demo:
    gr.Markdown("## 📄 AI Resume Analyzer")
    gr.Markdown("Paste a job description and resume text to get a skill match score (ATS-style).")

    with gr.Row():
        jd_box = gr.Textbox(
            lines=12,
            label="Job Description",
            placeholder="Paste the JD here...",
        )
        resume_box = gr.Textbox(
            lines=12,
            label="Resume Text",
            placeholder="Paste your resume here...",
        )

    analyze_btn = gr.Button("Analyze")

    matched_out = gr.HighlightedText(
        label="Matched Skills",
        show_legend=False,
    )
    missing_out = gr.Textbox(label="Missing Skills", interactive=False)
    match_percent_out = gr.Number(label="Skill Match (%)", interactive=False)
    final_score_out = gr.Number(label="Final ATS Score (0–100)", interactive=False)
    summary_out = gr.Textbox(label="Summary", lines=8, interactive=False)

    analyze_btn.click(
        fn=analyze_resume,
        inputs=[jd_box, resume_box],
        outputs=[matched_out, missing_out, match_percent_out, final_score_out, summary_out],
    )


if __name__ == "__main__":
    demo.launch()
