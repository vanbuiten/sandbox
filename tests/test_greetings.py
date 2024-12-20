import pytest
from fastapi.testclient import TestClient

from sandbox.main import app

client = TestClient(app)


@pytest.mark.parametrize("name", ["Alice", "Bob"])
def test_post_greetings(name: str) -> None:
    # Define the request payload
    request_payload = {"name": name}

    # Send a POST request to the /greetings endpoint
    response = client.post("/greetings", json=request_payload)

    # Assert the response status code
    assert response.status_code == 200

    # Assert the response data
    assert response.json() == {"hello": name}
