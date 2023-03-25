from fastapi.testclient import TestClient
from example_http_server.main import app
import json


def test_status_route():
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert response.json() == {"status": "serving"}
