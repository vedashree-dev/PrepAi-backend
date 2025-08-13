# routers/file_handler.py

from fastapi import APIRouter
from fastapi.responses import JSONResponse
from models.request_models import FileUploadRequest
from services.parser_service import parse_file_content
from utils.text_cleaner import clean_text_pipeline
from utils.chunker import chunk_text

router = APIRouter(prefix="/parse", tags=["Parsing"])


@router.post("/")
async def parse_uploaded_file(file_data: FileUploadRequest):
    try:
        raw_text = parse_file_content(file_data.file_name, file_data.content or "")
        cleaned = clean_text_pipeline(raw_text)
        chunks = chunk_text(cleaned)
        return JSONResponse(content={"cleaned_text": cleaned, "chunks": chunks}, status_code=200)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
