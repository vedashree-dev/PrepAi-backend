
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


# ✅ Import your routers
from routers import question_generator
from routers import regenerate_question
from routers import test_api
from routers import file_upload  # <-- This is the file_upload.py router
import os
app = FastAPI()

# ✅ Allow CORS for frontend communication
FRONTEND_ORIGIN = os.getenv("FRONTEND_ORIGIN")  # e.g. https://prepai.vercel.app

app.add_middleware(
    CORSMiddleware,
    allow_origins=[FRONTEND_ORIGIN] if FRONTEND_ORIGIN else ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Include all routers with correct prefixes
app.include_router(file_upload.router, prefix="/api/upload", tags=["File Upload"])
app.include_router(question_generator.router, prefix="/api/generate", tags=["Question Generation"])
app.include_router(regenerate_question.router, prefix="/api", tags=["Regenerate"])
app.include_router(test_api.router, prefix="/api/test", tags=["Test"])

@app.get("/")
def root():
    return {"message": "Welcome to PreppyAI backend"}

@app.get("/healthz")
def healthz():
    return {"ok": True}
