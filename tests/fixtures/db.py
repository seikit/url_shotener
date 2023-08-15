import pytest


@pytest.fixture(scope="session", autouse=True)
def setup():
    pass
    # subprocess.run(["docker compose up -d"], shell=True, check=True)
    # yield
    # subprocess.run(["docker compose down -v"], shell=True, check=True)
