from url_shortener.dao.url_redis import UrlRedis


def test_redis_set_data(get_redis):
    redis: UrlRedis = UrlRedis(redis=get_redis)

    result: str = redis.set(short="https://short-url.com", long="https://long-url.com")

    assert result is True


def test_redis_get_data(get_redis):
    redis: UrlRedis = UrlRedis(redis=get_redis)

    short: str = "https://short-url.com"
    long: str = "https://long-url.com"

    redis.set(short, long)

    data: str = redis.get(short)

    assert data == long
