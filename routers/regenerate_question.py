from fastapi import APIRouter
from pydantic import BaseModel
from services.question_templates import generate_single_question

router = APIRouter()

class RegenerateRequest(BaseModel):
    topic: str
    content: str
    type: str
    language: str
    difficulty: int
    instructions: str = ""

@router.post("/regenerate")
async def regenerate_question(request: RegenerateRequest):
    print("🌀 REGEN REQUEST:", request.dict())

    question = generate_single_question(
        title=request.topic,
        content=request.content,
        q_type=request.type,
        language=request.language,
        difficulty_level=request.difficulty,
        instructions=request.instructions
    )

    print("✅ GENERATED QUESTION:", question)
    return question
