from pydantic import BaseSettings

class Settings(BaseSettings):
    openai_api_key: str
    localai_api_endpoint: str
    cache_ttl: int = 300
    log_level: str = "INFO"
    log_file: str = "logs/chatbot.log"
    interaction_log_file: str = "logs/user_interactions.log"
    fine_tuned_model_dir: str = "./app/models/fine_tuned_bert"
    production_model_dir: str = "./app/models/production_model"
    training_interval: int = 3600  # 1 hour
    
    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'

settings = Settings()
