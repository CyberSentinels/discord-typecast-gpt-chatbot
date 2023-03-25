from fastapi.testclient import TestClient
from app.main import app
from app.models.bot import BotStatus

client = TestClient(app)


def test_about_bot():
    response = client.get("/about-bot")
    assert response.status_code == 200
    assert response.json() == {
        "name": "Compassionate Conversationalist Bot",
        "status": BotStatus.SERVING,
        "mission": "To compassionately serve its users"
    }
