# models/response_models.py

from typing import List, Dict, Optional
from pydantic import BaseModel


class ChunkedTextResponse(BaseModel):
    cleaned_text: str
    chunks: List[str]


class GeneratedQuestion(BaseModel):
    question_type: str
    marks: int
    question: str
    answer: Optional[str] = None
    difficulty: Optional[str] = None
    bloom_level: Optional[str] = None


class TopicQuestions(BaseModel):
    topic: str
    questions: List[GeneratedQuestion]


class FinalPaperResponse(BaseModel):
    sections: Dict[str, List[GeneratedQuestion]]
    total_marks: int
    answer_key: Optional[List[str]] = None
