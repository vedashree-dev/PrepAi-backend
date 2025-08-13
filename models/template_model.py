# models/template_model.py

from typing import List, Optional
from pydantic import BaseModel

class QuestionModel(BaseModel):
    type: str
    question: str
    marks: int
    answer: Optional[str] = None

class TopicModel(BaseModel):
    topic: str
    difficulty: str
    questions: List[QuestionModel]

class TemplateCreate(BaseModel):
    title: str
    paper: List[TopicModel]
    format: str  # "pdf" or "docx"
    include_answer_key: bool

class TemplateResponse(TemplateCreate):
    pass
