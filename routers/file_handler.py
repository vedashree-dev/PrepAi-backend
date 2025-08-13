# services/file_handler.py

from fastapi import APIRouter, UploadFile, File, HTTPException
from uuid import uuid4
import shutil
from pathlib import Path
from fastapi.responses import JSONResponse

from config import get_settings
from models.request_models import FileUploadRequest
from services.parser_service import parse_file_content
from utils.chunker import chunk_text
from utils.text_cleaner import clean_text_pipeline

router = APIRouter()
settings = get_settings()

SUPPORTED_TYPES = [
    "application/pdf",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    "text/plain"
]

# ---------- Route 1: Upload File ----------
@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    if file.content_type not in SUPPORTED_TYPES:
        raise HTTPException(status_code=400, detail="Unsupported file type")

    ext = Path(file.filename).suffix
    file_id = f"{uuid4()}{ext}"
    save_path = Path(settings.UPLOAD_DIR) / file_id
    save_path.parent.mkdir(parents=True, exist_ok=True)

    with open(save_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    return {
        "file_id": file_id,
        "filename": file.filename,
        "path": str(save_path),
        "content_type": file.content_type
    }

# ---------- Route 2: Parse Uploaded File ----------
from fastapi import Request

@router.post("")
async def parse_uploaded_file(request: Request):

    try:
        data = await request.json()
        print("🔥 Received at /parse:", data)  # 👈 This is what frontend is actually sending

        # simulate parsing the expected model
        from models.request_models import FileUploadRequest
        file_data = FileUploadRequest(**data)

        content_bytes = file_data.content.encode("utf-8")
        raw_text = parse_file_content(file_data.file_name, content_bytes)
        cleaned = clean_text_pipeline(raw_text)
        chunks = chunk_text(cleaned)

        return JSONResponse(content={
            "cleaned_text": cleaned,
            "chunks": chunks
        }, status_code=200)

    except Exception as e:
        print("❌ Error parsing:", e)
        return JSONResponse(content={"error": str(e)}, status_code=500)


   