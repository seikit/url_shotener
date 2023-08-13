from sqlalchemy import Column, Integer, String
from url_shortener.config.database import Base


class Url(Base):
    __tablename__ = "url"

    id = Column(Integer, primary_key=True, index=True)
    short_url = Column(String, index=True)
    long_url = Column(String, index=True)
