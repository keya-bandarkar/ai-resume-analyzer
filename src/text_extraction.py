import os

def extract_text(path: str) -> str:
    """
    Simple text extractor. v1 supports only .txt files.
    You can extend later for PDF/DOCX.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")

    with open(path, "r", encoding="utf-8") as f:
        return f.read()
