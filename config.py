from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    # LLM
    use_gpt_fallback: bool = False
    openai_api_key: str = ""
    ollama_base_url: str = "http://localhost:11434"
    ollama_model_name: str = "mistral"

    # Razorpay
    razorpay_enabled: bool = False
    razorpay_api_key: str = ""
    razorpay_api_secret: str = ""

    # Export paths
    EXPORT_DIR: str = "exports/"
    TEMPLATE_DIR: str = "templates/"
    STATIC_DIR: str = "static/"

    # Embedding
    embedding_model: str = "all-MiniLM-L6-v2"

    # Other
    debug: bool = True

    class Config:
        env_file = ".env"
        extra = "ignore"  # ✅ prevents error on unknown .env vars like PYTHONPATH

@lru_cache
def get_settings():
    return Settings()
