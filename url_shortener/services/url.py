from typing import Optional
from fastapi import HTTPException
from url_shortener.config.settings import settings
from url_shortener.dao.url import UrlDao
from url_shortener.dao.url_redis import UrlRedis
from url_shortener.schemas.url import UrlBase, UrlLong, UrlShort
from sqlalchemy.orm.session import Session
from url_shortener.models.url import Url
from url_shortener.utils import hash_it


class UrlService:
    def __init__(self, db: Session, cache: Optional[UrlRedis] = None):
        self.url_dao = UrlDao(db)
        self.r = cache

    def shorten(self, long_url: str) -> UrlShort:
        url: Url = self.url_dao.get_by_long_url(long_url)
        if url:
            return UrlShort(short_url=url.short_url)

        hashed: str = hash_it(long_url)

        url: UrlBase = UrlBase(
            short_url=f"{settings.base_domain}{hashed}",
            long_url=long_url,
        )
        return UrlShort(short_url=self.save_url(url).short_url)

    def save_url(self, url: UrlBase) -> Url:
        return self.url_dao.save(url)

    def get_long_url(self, short_url: str) -> UrlLong:
        db_url: Url = self.url_dao.get_by_short_url(short_url)
        if db_url is None:
            HTTPException(status_code=404, detail="URL not found.")
        return UrlLong(long_url=db_url.long_url)
