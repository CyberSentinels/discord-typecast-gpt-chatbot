from fastapi import APIRouter
from example_http_server.models.bot import BotStatus

router = APIRouter()


@router.get("/")
async def get_status():
    return {"status": BotStatus.SERVING}
