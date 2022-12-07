from pydantic import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    env_name: str = "Local"
    base_url: str = "http://localhost:4000"
    db_url: str = "sqlite:///./shortener.db"

    class Config:
        env_file = ".env"
        
    