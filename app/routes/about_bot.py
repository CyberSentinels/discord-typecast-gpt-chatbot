from fastapi import APIRouter
from app.models.bot import Bot, BotStatus

router = APIRouter()

@router.get("/about-bot", response_model=Bot)
async def get_about_bot():
    bot = Bot(
        name="Compassionate Conversationalist Bot",
        status=BotStatus.SERVING,
        mission="To compassionately serve its users"
    )
    return bot
