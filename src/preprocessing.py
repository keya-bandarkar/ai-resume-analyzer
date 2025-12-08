import re

def clean_text(text: str) -> str:
    """
    Lowercase, collapse whitespace, remove some special chars.
    """
    text = text.lower()
    text = re.sub(r"[\r\n]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()
