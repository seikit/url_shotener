from fastapi import HTTPException
from url_shortener.config.settings import settings
from url_shortener.dao.url import UrlDao
from url_shortener.schemas.url import UrlBase, UrlLong, UrlShort
from sqlalchemy.orm.session import Session
from url_shortener.models.url import Url


class UrlService:
    def __init__(self, db: Session):
        self.url_dao = UrlDao(db)

    def shorten(self, long_url: str) -> UrlShort:
        url: Url = self.url_dao.get_by_long_url(long_url)
        if url:
            return UrlShort(short_url=url.short_url)
        url: UrlBase = UrlBase(
            short_url=f"{settings.base_domain}{str(hash(long_url))[:6]}",
            long_url=long_url,
        )
        return UrlShort(short_url=self.save_url(url).short_url)

    def save_url(self, url: UrlBase) -> Url:
        return self.url_dao.save(url)

    def get_long_url(self, short_url: str) -> UrlLong:
        url: Url = self.url_dao.get_by_short_url(short_url)
        if url is None:
            HTTPException(status_code=404, detail="URL not found.")
        return UrlLong(long_url=url.long_url)
