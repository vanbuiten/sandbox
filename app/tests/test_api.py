from starlette.testclient import TestClient

from app.version import __version__

def test_root(client: TestClient):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {'version': __version__}


def test_health(client: TestClient):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json() == {'msg': "I'm healthy!"}
