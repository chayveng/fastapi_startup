from typing import List

from pydantic_settings import BaseSettings


class Configs(BaseSettings):
    # CORS
    BACKEND_CORS_ORIGINS: List[str] = ["*"]

    class Config:
        case_sensitive = True

class TestConfigs(Configs):
    ENV: str = "test"


configs = Configs()