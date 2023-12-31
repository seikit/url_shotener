import redis
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from url_shortener.config.settings import settings

SQLALCHEMY_DATABASE_URL = f"{settings.db_driver}://{settings.db_user}:{settings.db_pwd}@{settings.db_host}/{settings.database}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_redis():
    cache = redis.Redis(
        host=settings.redis_host,
        port=settings.redis_port,
        decode_responses=settings.decode_responses,
        password=settings.redis_pwd,
    )
    try:
        yield cache
    finally:
        cache.close()
