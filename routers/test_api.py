# routers/test_api.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def test():
    return {"status": "API working fine ✅"}

