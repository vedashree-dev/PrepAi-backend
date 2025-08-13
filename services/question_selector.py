from typing import List, Dict, Tuple
import random

def select_questions(question_pool: Dict[str, List[Dict]], total_marks: int, difficulty: str) -> List[Dict]:
    """
    Selects questions from the question pool to match total marks and difficulty balance.
    Organizes them into sections A/B/C.
    """
    selected = []
    marks_collected = 0

    # Define weights
    difficulty_weights = {
        'easy': {'easy': 0.6, 'medium': 0.3, 'hard': 0.1},
        'medium': {'easy': 0.3, 'medium': 0.5, 'hard': 0.2},
        'hard': {'easy': 0.2, 'medium': 0.4, 'hard': 0.4},
    }

    weights = difficulty_weights[difficulty]
    pool_flat = []

    for topic, questions in question_pool.items():
        for q in questions:
            q['topic'] = topic
            pool_flat.append(q)

    # Shuffle for randomness
    random.shuffle(pool_flat)

    # Group by difficulty
    grouped = {'easy': [], 'medium': [], 'hard': []}
    for q in pool_flat:
        grouped[q['difficulty']].append(q)

    # Define selection priority (based on marks)
    priority = [5, 3, 2, 1]

    while marks_collected < total_marks:
        for diff_level in ['easy', 'medium', 'hard']:
            candidates = grouped[diff_level]
            for mark in priority:
                for q in candidates:
                    if q['marks'] == mark and q not in selected:
                        selected.append(q)
                        marks_collected += mark
                        break
                if marks_collected >= total_marks:
                    break
            if marks_collected >= total_marks:
                break

    # Sectionization
    sections = {'A': [], 'B': [], 'C': []}
    for q in selected:
        if q['marks'] == 1:
            sections['A'].append(q)
        elif q['marks'] in [2, 3]:
            sections['B'].append(q)
        else:
            sections['C'].append(q)

    return sections
