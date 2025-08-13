from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from pydantic import BaseModel
from typing import Optional, List
import json

router = APIRouter()

# Request model for settings (used by frontend)
class PaperSettings(BaseModel):
    total_marks: int
    question_types: List[str]  # e.g., ["MCQ", "Short", "Long", "HOTS"]
    difficulty: int  # 0 to 100
    language: str = "English"
    sample_paper_structure: Optional[dict] = None

@router.post("/submit")
async def submit_settings(settings: PaperSettings):
    # Save settings or process them to pass into question generator
    return {
        "status": "success",
        "message": "Settings received.",
        "config": settings
    }

@router.post("/upload-sample")
async def upload_sample_paper(file: UploadFile = File(...)):
    if not file.filename.endswith((".pdf", ".docx", ".txt")):
        raise HTTPException(status_code=400, detail="Only PDF, DOCX, or TXT sample papers are supported.")

    try:
        # In production, parse the structure: section names, marks per section, type count, etc.
        content = await file.read()
        return {
            "status": "success",
            "message": "Sample uploaded. Structure detection logic will go here.",
            "structure_detected": {
                "Section A": {"type": "MCQ", "marks": 10, "count": 10},
                "Section B": {"type": "Short", "marks": 20, "count": 5},
                "Section C": {"type": "Long", "marks": 50, "count": 5}
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/default-settings")
async def get_default_settings():
    return {
        "total_marks_options": [10, 20, 40, 80],
        "question_types": ["MCQ", "Short", "Long", "HOTS"],
        "difficulty_range": {"min": 0, "max": 100},
        "languages": ["English", "Hindi", "French"]
    }
