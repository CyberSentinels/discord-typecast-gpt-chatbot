from fastapi import APIRouter
from app.models.bot import BotStatus

router = APIRouter()


@router.get("/")
async def get_status():
    return {"status": BotStatus.SERVING}
