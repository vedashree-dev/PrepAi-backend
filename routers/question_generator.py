# routers/question_generator.py

from urllib import request
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict
from models.request_models import FileUploadRequest, GenerationSettings
from services.concept_extractor import extract_concepts
from services.question_templates import generate_questions_for_topic
from utils.difficulty_labeler import label_difficulty
from fastapi import UploadFile, File

router = APIRouter()

class PaperGenerationRequest(BaseModel):
    file: FileUploadRequest
    settings: GenerationSettings

@router.post("/")
async def generate_paper(request: PaperGenerationRequest):
    try:
        # Extract chunks from file content
        chunks = request.file.content.split("\n\n")
        parsed_chunks = [
            {"heading": f"Topic {i + 1}", "content": chunk.strip()}
            for i, chunk in enumerate(chunks) if chunk.strip()
        ]

        # Extract concepts
        concepts = extract_concepts(parsed_chunks)

        all_questions = []
        enabled_types = {
    t.upper(): v["count"]
    for t, v in request.settings.question_types.items()
    if v.get("enabled")
}

        for topic in concepts:
          difficulty = label_difficulty([topic["content"]])[0]
        questions = generate_questions_for_topic(
        title=topic["title"],
        content=topic["content"],
        type_counts=enabled_types,
        language=request.settings.language,
        difficulty_level=difficulty,
    )


        all_questions.append({
                "topic": topic["title"],
                "difficulty": difficulty,
                "questions": questions,
            })

        return {
            "total_requested_marks": request.settings.total_marks,
            "question_types": request.settings.question_types,
            "language": request.settings.language,
            "paper": all_questions
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

print("Received request:", request)


@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    content = (await file.read()).decode("utf-8")
    return {
        "file_id": "123",
        "file_name": file.filename,
        "content_type": file.content_type,
        "raw_text": content,
    }