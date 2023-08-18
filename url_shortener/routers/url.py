from fastapi import APIRouter, Depends
from redis import Redis
from sqlalchemy.orm import Session
from url_shortener.config.database import get_db, get_redis
from url_shortener.schemas.url import UrlLong, UrlShort
from url_shortener.services.url import UrlService

router = APIRouter()


@router.post("/shorten", response_model=UrlShort)
def create_short_url(
    long_url: str, db: Session = Depends(get_db), cache: Redis = Depends(get_redis)
) -> str:
    return UrlService(db, cache).shorten(long_url)


@router.get("/short-url", response_model=UrlLong)
def get_long_url(
    short_url: str, db: Session = Depends(get_db), cache: Redis = Depends(get_redis)
) -> str:
    return UrlService(db, cache).get_long_url(short_url)
