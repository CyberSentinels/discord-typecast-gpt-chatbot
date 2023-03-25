from fastapi.testclient import TestClient
from example_http_server.main import app
from example_http_server.models.bot import BotStatus

client = TestClient(app)


def test_about_bot():
    response = client.get("/about-bot")
    assert response.status_code == 200
    assert response.json() == {
        "name": "Compassionate Conversationalist Bot",
        "status": BotStatus.SERVING,
        "mission": "To compassionately serve its users"
    }
