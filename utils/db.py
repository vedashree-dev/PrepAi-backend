import json
import os

TEMPLATE_DB = "templates.json"

def load_templates():
    if not os.path.exists(TEMPLATE_DB):
        with open(TEMPLATE_DB, "w") as f:
            json.dump([], f)
    with open(TEMPLATE_DB, "r") as f:
        return json.load(f)

def save_templates(templates):
    with open(TEMPLATE_DB, "w") as f:
        json.dump(templates, f, indent=2)

def add_template(template):
    templates = load_templates()
    templates.append(template)
    save_templates(templates)

def get_template_by_title(title):
    templates = load_templates()
    for temp in templates:
        if temp["title"].lower() == title.lower():
            return temp
    return None
