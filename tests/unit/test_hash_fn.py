from url_shortener.utils import hash_it


def test_hash_fn():
    long_url: str = "https://dummy-url.com"
    hashed: str = hash_it(long_url)
    assert isinstance(hashed, str)
    assert len(hashed) == 6
