from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from url_shortener.config.database import get_db
from url_shortener.schemas.url import UrlLong, UrlShort
from url_shortener.services.url import UrlService

router = APIRouter()


@router.post("/shorten", response_model=UrlShort)
def create_short_url(long_url: str, db: Session = Depends(get_db)) -> str:
    return UrlService(db).shorten(long_url)


@router.get("/short-url", response_model=UrlLong)
def get_long_url(short_url: str, db: Session = Depends(get_db)) -> str:
    return UrlService(db).get_long_url(short_url)
