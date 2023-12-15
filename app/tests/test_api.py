from starlette.testclient import TestClient

from app.api import app
from app.version import __version__

client = TestClient(app)


def test_root():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {'version': __version__}


def test_health():
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json() == {'msg': "I'm healthy!"}
