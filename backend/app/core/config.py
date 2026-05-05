from typing import List
from pydantic import AnyHttpUrl, Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    PROJECT_NAME: str = "Food Store API"
    API_V1_STR: str = "/api/v1"
    
    # Database
    DATABASE_URL: str = Field(..., validation_alias="DATABASE_URL")
    
    # Security
    SECRET_KEY: str = Field(..., validation_alias="SECRET_KEY")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    
    # CORS
    CORS_ORIGINS: List[str] = ["http://localhost:5173", "http://localhost:3000"]
    
    # MercadoPago
    MP_ACCESS_TOKEN: str = Field(..., validation_alias="MP_ACCESS_TOKEN")
    MP_PUBLIC_KEY: str = Field(..., validation_alias="MP_PUBLIC_KEY")
    MP_NOTIFICATION_URL: str = Field(..., validation_alias="MP_NOTIFICATION_URL")
    
    model_config = SettingsConfigDict(
        env_file=".env", 
        env_file_encoding="utf-8",
        case_sensitive=True
    )

@lru_cache()
def get_settings() -> Settings:
    return Settings()

settings = get_settings()
