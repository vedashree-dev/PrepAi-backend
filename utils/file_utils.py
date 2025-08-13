# utils/file_utils.py

import fitz  # PyMuPDF
import docx

def extract_text_from_pdf(file_path: str) -> str:
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()
    return text

def extract_text_from_docx(file_path: str) -> str:
    doc = docx.Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs if para.text.strip()])

# utils/file_utils.py

def is_pdf(filename: str) -> bool:
    return filename.lower().endswith(".pdf")


def is_docx(filename: str) -> bool:
    return filename.lower().endswith(".docx")


def is_text(filename: str) -> bool:
    return filename.lower().endswith(".txt") or filename.lower().endswith(".text")
