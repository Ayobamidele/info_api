from pydantic_settings import BaseSettings
from decouple import config
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent.parent


class Settings(BaseSettings):
    PROJECT_NAME :str = "Info API"
    PROJECT_VERSION : str = "1.0.0"
    PROJECT_DESCRIPTION: str = "A Public API to Retrieve Basic Information"
    
    EMAIL: str = config("EMAIL", "Null")
    GITHUB_URL: str = config("GITHUB_URL", "Null")

 

settings = Settings()
