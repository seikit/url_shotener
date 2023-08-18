from redis import Redis


class UrlRedis:
    def __init__(self, redis: Redis) -> None:
        self.r = redis

    def get(self, short: str) -> str:
        return self.r.get(short)

    def set(self, short: str, long: str) -> None:
        self.r.set(name=short, value=long)
