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
        short: str = f"{settings.base_domain}{hash_it(long_url)}"

        cache_url: str = self.r.get(short)
        if cache_url:
            return UrlShort(short)

        db_url: Url = self.url_dao.get_by_short_url(short)
        if db_url:
            return UrlShort(db_url.short_url)

        url: UrlBase = UrlBase(
            short_url=short,
            long_url=long_url,
        )

        url: Url = self.save_url(url)
        self.r.set(url.short_url, url.long_url)

        return UrlShort(short_url=url.short_url)

    def save_url(self, url: UrlBase) -> Url:
        return self.url_dao.save(url)

    def get_long_url(self, short_url: str) -> UrlLong:
        cache_url: str = self.r.get(short_url)
        if cache_url:
            return UrlLong(long_url=cache_url)

        db_url: Url = self.url_dao.get_by_short_url(short_url)
        if db_url is None:
            HTTPException(status_code=404, detail="URL not found.")
        return UrlLong(long_url=db_url.long_url)
