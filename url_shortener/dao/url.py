from sqlalchemy.orm.session import Session
from url_shortener.models.url import Url
from url_shortener.schemas.url import UrlBase


class UrlDao:
    def __init__(self, db: Session):
        self.db = db
        self.model: Url = Url

    def get_by_long_url(self, long_url: str) -> Url:
        return self.db.query(self.model).filter(self.model.long_url == long_url).first()

    def get_by_short_url(self, short_url: str) -> Url:
        return (
            self.db.query(self.model).filter(self.model.short_url == short_url).first()
        )

    def save(self, url: UrlBase) -> Url:
        url: Url = Url(**url.model_dump())
        self.db.add(url)
        self.db.commit()
        self.db.refresh(url)
        return url
