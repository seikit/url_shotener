from typing import List
import pytest


@pytest.fixture
def data() -> List[str]:
    return [f"https://dummy-long-url.com/{i}" for i in range(5)]
