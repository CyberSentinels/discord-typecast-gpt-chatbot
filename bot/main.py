import os
import discord
from dotenv import load_dotenv
from controllers.message.handle_message import handle_message
load_dotenv()

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if client.user.mentioned_in(message):
        try:
            await handle_message(message)
        except Exception as e:
            await message.channel.send(
                embed=discord.Embed(
                    type="rich",
                    title="discord bot error",
                    description=f"{e}",
                    color=discord.Colour.brand_red()
                )
            )

DISCORD_BOT_APP_TOKEN = os.getenv("DISCORD_BOT_APP_TOKEN")
client.run(DISCORD_BOT_APP_TOKEN)
