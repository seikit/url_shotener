import subprocess
from time import sleep
import alembic
from fastapi.testclient import TestClient
import pytest
from alembic.config import Config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import app
from url_shortener.config.database import get_db

from url_shortener.config.settings import settings

TEST_DB = settings.test_db_conn

engine = create_engine(TEST_DB)
TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    try:
        db = TestSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


@pytest.fixture
def client():
    return TestClient(app)


def start_up_test_container() -> None:
    subprocess.run(
        "docker-compose -f docker-compose-test.yml up -d",
        shell=True,
        capture_output=True,
        text=True,
    )
    sleep(settings.max_wait)


def run_migrations() -> None:
    alembic_cfg = Config("alembic.ini")
    alembic_cfg.set_main_option("sqlalchemy.url", str(settings.test_db_conn))
    alembic.command.upgrade(alembic_cfg, "head")
    sleep(settings.max_wait)


def shutdown_test_container() -> None:
    subprocess.run(
        "docker-compose down -v --remove-orphans",
        shell=True,
        capture_output=True,
        text=True,
    )


@pytest.fixture(scope="session", autouse=True)
def setup():
    start_up_test_container()
    run_migrations()

    yield

    shutdown_test_container()
