import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize

nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)

stop_words = set(stopwords.words("english"))

def remove_headers_footers(text: str) -> str:
    lines = text.split("\n")
    content_lines = []
    for line in lines:
        # Remove common header/footer patterns (e.g., page numbers, titles repeated on every page)
        if re.match(r'^\s*(page)?\s*\d+\s*$', line.strip(), re.IGNORECASE):
            continue
        if len(line.strip()) < 4:
            continue
        content_lines.append(line)
    return "\n".join(content_lines)

def fix_paragraph_breaks(text: str) -> str:
    # Merge lines that were broken mid-sentence (common in PDFs)
    paragraphs = text.split("\n")
    fixed = []
    buffer = ""
    for line in paragraphs:
        line = line.strip()
        if not line:
            if buffer:
                fixed.append(buffer)
                buffer = ""
        else:
            if buffer and not buffer.endswith(('.', ':', '?')):
                buffer += " " + line
            else:
                if buffer:
                    fixed.append(buffer)
                buffer = line
    if buffer:
        fixed.append(buffer)
    return "\n\n".join(fixed)

def clean_text_pipeline(text: str) -> str:
    text = remove_headers_footers(text)
    text = fix_paragraph_breaks(text)

    # Remove weird characters and fix spacing
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^\x00-\x7F]+', ' ', text)

    return text.strip()
