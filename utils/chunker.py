import re
from nltk.tokenize import sent_tokenize

def split_by_headings(text: str) -> list[str]:
    """
    Split text based on headings like '1.1 Introduction', 'Chapter 3', or bold/uppercase lines.
    """
    lines = text.split("\n")
    chunks = []
    current_chunk = []

    heading_pattern = re.compile(r"^(chapter\s*\d+|[0-9]+\.\s*[\w\s]+|[A-Z][A-Z\s]{5,})$", re.IGNORECASE)

    for line in lines:
        line = line.strip()
        if heading_pattern.match(line):
            if current_chunk:
                chunks.append("\n".join(current_chunk).strip())
                current_chunk = []
        current_chunk.append(line)

    if current_chunk:
        chunks.append("\n".join(current_chunk).strip())

    return [chunk for chunk in chunks if len(chunk.split()) > 30]  # discard tiny ones

def sentence_chunking(text: str, max_words=120) -> list[str]:
    """
    Further splits large chunks into smaller ones based on sentence count or word limit.
    """
    sentences = sent_tokenize(text)
    chunks = []
    current = []

    current_len = 0
    for sentence in sentences:
        word_count = len(sentence.split())
        if current_len + word_count > max_words:
            chunks.append(" ".join(current))
            current = []
            current_len = 0
        current.append(sentence)
        current_len += word_count

    if current:
        chunks.append(" ".join(current))

    return chunks

def chunk_text(text: str) -> list[str]:
    """
    Full pipeline: detect topic boundaries and split into manageable subchunks.
    """
    heading_chunks = split_by_headings(text)
    all_chunks = []

    for chunk in heading_chunks:
        all_chunks.extend(sentence_chunking(chunk))

    return [c.strip() for c in all_chunks if len(c.strip()) > 30]
