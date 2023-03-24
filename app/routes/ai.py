import os
import openai
from fastapi import APIRouter
from dotenv import load_dotenv
load_dotenv()

router = APIRouter()


@router.get("/ai")
async def get_ai():
    openai.api_key = os.getenv("OPENAI_API_KEY")
    openai.Model.list()
    return openai.Model.list()
