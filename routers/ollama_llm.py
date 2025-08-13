from fastapi import APIRouter

router = APIRouter()

@router.get("/test-ollama")
async def test_ollama():
    return {"message": "Ollama route is working!"}
