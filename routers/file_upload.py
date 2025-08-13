# routers/file_upload.py
from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import JSONResponse
from services.file_handler import handle_uploaded_file
import uuid

router = APIRouter()

@router.post("/")
async def upload_file(file: UploadFile = File(...)):
    try:
        content = await file.read()
        file_id = str(uuid.uuid4())
        parsed_data = handle_uploaded_file(file.filename, content, file_id)
        return JSONResponse(content=parsed_data, status_code=200)
    except Exception as e:
        print("[ERROR during file upload]:", e)
        return JSONResponse(content={"error": str(e)}, status_code=500)

@router.post("/pasted")
async def upload_pasted_text(file_name: str = Form(...), content: str = Form(...)):
    try:
        file_id = str(uuid.uuid4())
        parsed_data = handle_uploaded_file(file_name, content.encode("utf-8"), file_id)
        return JSONResponse(content=parsed_data, status_code=200)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
