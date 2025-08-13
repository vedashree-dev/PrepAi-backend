from typing import Dict, List
import ollama
import json
from lib.ollama import call_llm 




def generate_questions_for_topic(
    title: str,
    content: str,
    type_counts: Dict[str, int],
    language: str = "English",
    difficulty_level: str = "Medium"
) -> List[Dict]:
    prompt = f"""
You are a helpful exam assistant AI that creates high-quality exam questions.

Topic Title: {title}

Content:
\"\"\"
{content}
\"\"\"

Generate the following number of questions per type:
{json.dumps(type_counts, indent=2)}

Each question should include:
- "type": (e.g., MCQ, SHORT, LONG, HOTS)
- "marks": 1 for MCQ, 2 for SHORT, 5 for LONG, 3 for HOTS
- "question": the question text
- "answer": a relevant, concise answer

Use only the content above. Match the {difficulty_level} level and use {language}.

Respond with a JSON array of question objects. No extra text.
"""

    try:
        response = ollama.chat(
            model="mistral",
            messages=[{"role": "user", "content": prompt}]
        )
        return json.loads(response["message"]["content"])

    except Exception as e:
        print("⚠️ Generation failed:", e)
        return [{
            "type": "ERROR",
            "marks": 0,
            "question": "Failed to generate questions.",
            "answer": str(e)
        }]

def generate_single_question(
    title: str,
    content: str,
    q_type: str,
    language: str = "English",
    difficulty_level: str = "Medium",
    instructions: str = ""
):
    
    prompt = f"""
Topic: {title}
Content: {content}

Generate one {q_type} question in {language} at {difficulty_level} difficulty.
Instructions: {instructions}

Respond in JSON format:
{{"type": "...", "marks": ..., "question": "...", "answer": "..."}} 
    """

    return call_llm(prompt, expected_format="json")


