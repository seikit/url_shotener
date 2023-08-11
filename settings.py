from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # App
    app_name: str = "URL SHORTENER"
    summary: str = "Learning project to understand url shortener system design."

    # DB
    db_driver: str = "postgresql"
    host: str
    user: str
    pwd: str
    database: str

    # Uvicorn
    host: str = "0.0.0.0"
    port: int = 8080


settings = Settings()
