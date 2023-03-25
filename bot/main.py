import os
import discord
import datetime
from discord import Activity, ActivityType, Status, app_commands, Embed
from discord.ext import commands, tasks
from dotenv import load_dotenv
from controllers.handle_message import handle_message

try:
    load_dotenv()
except Exception as e:
    print(f"Warning: Failed to load .env file. Continuing without it. Error: {e}")

DISCORD_BOT_APP_TOKEN = os.getenv("DISCORD_BOT_APP_TOKEN")

if not DISCORD_BOT_APP_TOKEN:
    raise ValueError(
        "DISCORD_BOT_APP_TOKEN not found in environment. Please set it in your .env file, as an environment variable, or another configuration method."
    )

# setup the discord.py client and intents
intents = discord.Intents.all()
intents.message_content = True
client = commands.Bot(command_prefix=["!", "/"], intents=intents)


@client.event
async def on_ready():
    # Print a message indicating that the bot is logged in and ready
    print(f"We have logged in as {client.user}")
    print("\nLogged in as:")
    print(" Username", client.user.name)
    print(" User ID", client.user.id)
    print(
        "To invite the bot in your server use this link:\n https://discord.com/api/oauth2/authorize?client_id="
        + str(client.user.id)
        + "&permissions=8&scope=bot%20applications.commands"
    )
    print("Time now", str(datetime.datetime.now()))

    try:
        synced = await client.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

    activity = Activity(
        type=ActivityType.streaming,
        name="@ me for help",
        url="https://cybersentinels.org/",
        state="Creating Content",
        details="Creating Content for the Cyber Sentinels",
        emoji=None,
    )
    await client.change_presence(activity=activity, status=Status.online)


@client.event
async def on_message(message):
    if client.user.mentioned_in(message):
        try:
            await handle_message(message)
        except Exception as e:
            await message.channel.send(
                embed=discord.Embed(
                    type="rich",
                    title="Discord bot error",
                    description=f"{e}",
                    color=discord.Colour.red(),
                )
            )


try:
    client.run(DISCORD_BOT_APP_TOKEN)
except Exception as e:
    print(f"Error while running the bot: {e}")
