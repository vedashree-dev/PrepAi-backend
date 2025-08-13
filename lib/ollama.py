import subprocess
import json

def call_llm(prompt: str, expected_format: str = None, model: str = "llama3") -> dict:


    try:
        result = subprocess.run(
            ["ollama", "run", model],
            input=prompt.encode(),
            capture_output=True,
            timeout=60
        )
        output = result.stdout.decode().strip()

        json_start = output.find("{")
        json_end = output.rfind("}")
        json_str = output[json_start:json_end+1]

        return json.loads(json_str)
    except Exception as e:
        print("❌ Error during LLM call:", e)
        return {
            "type": "ERROR",
            "marks": 0,
            "question": "Failed to generate",
            "answer": str(e)
        }
