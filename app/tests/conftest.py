from typing import Generator

import pytest
from starlette.testclient import TestClient

from app.api import app
from app.db.session import SessionLocal


@pytest.fixture
def client() -> Generator:
    yield TestClient(app)

@pytest.fixture(scope='session')
def db() -> Generator:
    yield SessionLocal()
