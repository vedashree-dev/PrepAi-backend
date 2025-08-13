# services/concept_extractor.py

import re
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize import sent_tokenize
from typing import List


def extract_concepts(chunks: List[dict]) -> List[dict]:
    """
    Extracts top concepts from each chunk using TF-IDF + sentence scoring.
    Returns a list of dicts with 'title' and 'content' per concept.
    """

    concepts = []

    for chunk in chunks:
        title = chunk["heading"]
        content = chunk["content"]

        # Split into sentences
        sentences = sent_tokenize(content)

        if not sentences:
            continue

        # TF-IDF over all sentences
        vectorizer = TfidfVectorizer()
        try:
            tfidf_matrix = vectorizer.fit_transform(sentences)
        except Exception:
            continue

        # Take top 2 scored sentences
        scores = tfidf_matrix.sum(axis=1).A1
        top_indices = scores.argsort()[-2:][::-1]
        selected = " ".join([sentences[i] for i in top_indices])

        concepts.append({
            "title": title,
            "content": selected.strip()
        })

    return concepts
