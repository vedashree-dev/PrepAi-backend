# services/parser_service.py

import os
import docx2txt
import fitz  # PyMuPDF
from utils.file_utils import is_pdf, is_docx, is_text

def parse_file(file_name: str, file_type: str, content: str):
    if not content:
        raise ValueError("Uploaded file content is empty or invalid")

    # existing logic continues...


def parse_file_content(filename: str, content: bytes) -> str:
    """
    Main parser that detects file type and extracts text accordingly.
    """
    if is_pdf(filename):
        return parse_pdf(content)
    elif is_docx(filename):
        return parse_docx(content)
    elif is_text(filename):
        return parse_text(content)
    else:
        raise ValueError("Unsupported file format")


def parse_pdf(content: bytes) -> str:
    """Extracts text from a PDF using PyMuPDF."""
    text = ""
    with fitz.open("pdf", content) as doc:
        for page in doc:
            text += page.get_text()
    return text


def parse_docx(content: bytes) -> str:
    """Extracts text from DOCX using docx2txt."""
    import tempfile
    with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as tmp:
        tmp.write(content)
        tmp_path = tmp.name
    text = docx2txt.process(tmp_path)
    os.remove(tmp_path)
    return text


def parse_text(content: bytes) -> str:
    """Handles pasted/plain text input."""
    return content.decode("utf-8")
