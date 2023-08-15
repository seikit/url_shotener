from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    # App
    app_name: str = "URL SHORTENER"
    summary: str = "Learning project to understand url shortener system design."

    # DB
    db_driver: str = "postgresql"
    db_host: str
    db_user: str
    db_pwd: str
    database: str

    # Uvicorn
    app: str = "main:app"
    host: str = "0.0.0.0"
    port: int = 8080
    reload: bool = False
    workers: int = 2

    # URL
    base_domain: str = "https://short-url/"


settings = Settings()
