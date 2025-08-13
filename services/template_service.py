# services/template_service.py

from utils.db import add_template, get_template_by_title
from models.template_model import TemplateCreate, TemplateResponse


def save_template_service(template_data: TemplateCreate) -> dict:
    """
    Save a paper template to the JSON DB.
    """
    add_template(template_data.dict())
    return {"message": "Template saved successfully"}


def load_template_service(title: str) -> dict:
    """
    Load a paper template by title.
    """
    template = get_template_by_title(title)
    if template:
        return TemplateResponse(**template)
    return {"error": "Template not found"}
