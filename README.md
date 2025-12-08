# AI Resume Analyzer

A simple ATS-style resume analyzer that compares a candidate's resume to a job description and computes a compatibility score based on skill overlap.

## Features

- Extracts text from plain-text resumes and job descriptions.
- Uses a custom skills dictionary to detect relevant technical skills.
- Computes:
  - Skills required in the job description
  - Skills present in the resume
  - Missing skills
  - An ATS-style score between 0 and 100

## Project Structure

- `data/resumes/` – sample resumes (currently .txt)
- `data/job_descriptions/` – sample job description files
- `data/skills_dictionary.csv` – list of skills and categories
- `src/` – core source code (config, text extraction, preprocessing, skill matching, scoring, app)

## How to Run

```bash
python -m venv venv
venv\Scripts\activate  # or source venv/bin/activate on Mac/Linux
pip install -r requirements.txt

python -m src.app
