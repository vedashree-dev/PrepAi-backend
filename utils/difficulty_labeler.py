# services/difficulty_labeler.py

import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
import numpy as np

# Ensure necessary downloads
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)

stop_words = set(stopwords.words("english"))
punctuations = set(string.punctuation)

def label_difficulty(texts: list[str]) -> list[str]:
    """
    Labels a list of texts as Easy/Medium/Hard using heuristics.
    Used during paper generation.
    """
    results = []
    for text in texts:
        wc = len(text.split())
        if wc < 100:
            results.append("Easy")
        elif wc < 200:
            results.append("Medium")
        else:
            results.append("Hard")
    return results


def preprocess_text(text):
    """Tokenizes, removes stopwords and punctuation."""
    tokens = word_tokenize(text.lower())
    return [word for word in tokens if word not in stop_words and word not in punctuations and word.isalpha()]

def compute_tfidf_difficulty(concepts, source_text):
    """
    Uses TF-IDF vectorization to assign difficulty to each concept
    based on how rare/complex it is in the source material.
    """
    if not concepts or not source_text:
        return {concept: "Medium" for concept in concepts}

    processed_concepts = [" ".join(preprocess_text(c)) for c in concepts]
    source_docs = [source_text] + processed_concepts

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(source_docs)

    # Concept TF-IDF vectors (skip first which is source_text)
    concept_vectors = tfidf_matrix[1:]

    # Mean TF-IDF value for each concept
    mean_scores = concept_vectors.mean(axis=1).A1

    labeled = {}
    for i, concept in enumerate(concepts):
        score = mean_scores[i]
        if score < 0.05:
            label = "Easy"
        elif score < 0.12:
            label = "Medium"
        else:
            label = "Hard"
        labeled[concept] = label

    return labeled
