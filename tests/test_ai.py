from fastapi.testclient import TestClient
from app.main import app
import json


def test_ai_route():
    client = TestClient(app)
    response = client.get("/ai")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert response.json() == {"message": "hello, world!"}
