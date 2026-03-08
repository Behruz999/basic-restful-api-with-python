from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # PROJECT_NAME: str = "FastAPI Template"
    # API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "RestPy"
    DATABASE_URL: str = "sqlite:///./restpy.db"
    DEBUG: bool = False
    API_V1_PREFIX: str = "/api/v1"

    class Config:
        env_file = ".env"
        # extra = "allow"


settings = Settings()
