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

    # Max wait time
    max_wait: int = 2

    # Redis
    redis_host: str
    redis_port: int
    redis_pwd: str
    decode_responses: bool = True

    ## Test environment
    # Redis Test
    test_redis_host: str = "localhost"
    test_redis_port: int = 6370
    test_redis_pwd: str = "pwd_test_redis_1234"
    test_redis_decode_responses: bool = True

    # TEST_DB_CONN
    test_db_conn: str = (
        "postgresql://test_dev_user:test_pwd_1234@localhost:5430/test_url_shortener"
    )


settings = Settings()
