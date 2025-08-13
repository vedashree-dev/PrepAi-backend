# models/request_models.py

from typing import Dict, Optional
from pydantic import BaseModel


class FileUploadRequest(BaseModel):
    file_name: str
    file_type: str  # pdf, docx, txt
    content: Optional[str] = None  # Used for pasted plain text

class GenerationSettings(BaseModel):
    total_marks: int
    difficulty: int
    language: str
    question_types: Dict[str, Dict[str, int | bool]]
    generate_answer_key: bool = False
    template_id: Optional[str] = None


class PaperGenerationRequest(BaseModel):
    file: FileUploadRequest
    settings: GenerationSettings
