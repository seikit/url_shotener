from pydantic import BaseModel


class UrlBase(BaseModel):
    short_url: str
    long_url: str


class Url(UrlBase):
    id: int

    class Config:
        orm_mode = True


class UrlShort(BaseModel):
    short_url: str


class UrlLong(BaseModel):
    long_url: str
