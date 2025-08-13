# services/file_handler.py

from services.parser_service import parse_file_content
from utils.text_cleaner import clean_text_pipeline
from fastapi import UploadFile
from typing import List


def handle_uploaded_file(filename: str, content: bytes, file_id: str):
    """
    Handles a single uploaded file. Detects type and routes to parser,
    returns cleaned text for display or generation.
    """
    parsed_text = parse_file_content(filename, content)
    cleaned_text = clean_text_pipeline(parsed_text)

    return {
        "file_id": file_id,
        "file_name": filename,
        "raw_text": cleaned_text
    }


def process_uploaded_files(files: List[UploadFile]) -> str:
    """
    Handles multiple uploaded files. Cleans and combines their contents.
    """
    combined_text = ""

    for file in files:
        filename = file.filename.lower()
        file_bytes = file.file.read()

        try:
            raw_text = parse_file_content(filename, file_bytes)
            cleaned_text = clean_text_pipeline(raw_text)
            combined_text += cleaned_text + "\n\n"
        except Exception as e:
            print(f"[!] Error processing {filename}: {e}")
            continue

    return combined_text.strip()
