def hash_it(long_url: str) -> str:
    return str(hash(long_url))[:6]
