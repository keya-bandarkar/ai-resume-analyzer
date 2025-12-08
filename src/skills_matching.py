import pandas as pd
from typing import List

def load_skills(skill_file: str) -> list[str]:
    df = pd.read_csv(skill_file)
    return df["skill"].str.lower().tolist()

def extract_present_skills(text: str, skills: List[str]) -> list[str]:
    """
    Very simple presence check: substring-based.
    You can later improve this using tokenization / regex.
    """
    present = []
    for skill in skills:
        if skill in text:
            present.append(skill)
    return present
