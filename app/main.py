from fastapi import FastAPI
from .routes import status, about_bot, ai

app = FastAPI()

app.include_router(status.router)
app.include_router(about_bot.router)
app.include_router(ai.router)
