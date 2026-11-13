import os
from pathlib import Path
from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    base_url: str = Field(default="https://example.com", alias="BASE_URL")
    headless: bool = Field(default=True, alias="HEADLESS")
    browser: str = Field(default="chromium", alias="BROWSER")
    slowmo: int = Field(default=0, alias="SLOWMO")
    timeout: int = Field(default=30000, alias="TIMEOUT")
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False

settings = Settings()