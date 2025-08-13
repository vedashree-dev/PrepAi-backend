# models/export_model.py

from typing import List, Optional
from pydantic import BaseModel


class ExportQuestion(BaseModel):
    number: int
    question: str
    marks: int
    section: str
    answer: Optional[str] = None


class ExportPaper(BaseModel):
    title: str
    total_marks: int
    questions: List[ExportQuestion]
    show_answer_key: bool = False
