from fastapi.testclient import TestClient

from sandbox.main import app
from sandbox.utils import get_version

client = TestClient(app)


def test_read_root() -> None:
    # Send a gte request to the / endpoint
    response = client.get("/")

    # Assert the response status code
    assert response.status_code == 200

    version = get_version()

    # Assert the response data
    assert response.json() == {"status": "ok", "version": version}
