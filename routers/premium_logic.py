from fastapi import APIRouter
from models.template_model import TemplateCreate
from services.template_service import save_template_service, load_template_service

router = APIRouter()

@router.post("/save-template")
def save_template(template: TemplateCreate):
    return save_template_service(template)

@router.get("/load-template/{title}")
def load_template(title: str):
    return load_template_service(title)
