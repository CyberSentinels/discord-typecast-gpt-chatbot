import asyncio
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


# Add global dictionaries for tracking user and server question counts
user_question_count = {}
server_question_count = {}
user_count_limit = 5
server_count_limit = 100

@client.event
async def on_message(message):
    global user_question_count, server_question_count
    if client.user.mentioned_in(message):
        # Check if the user has admin permissions
        author_perms = message.author.permissions_in(message.channel)
        if not author_perms.administrator:
            # Increment user and server question counts
            user_question_count[message.author.id] = user_question_count.get(message.author.id, 0) + 1
            server_question_count[message.guild.id] = server_question_count.get(message.guild.id, 0) + 1
            userfailcondition = user_question_count[message.author.id] > user_count_limit
            serverfailcondition = server_question_count[message.guild.id] > server_count_limit
            if userfailcondition:
                faildescription = f"You have reached the daily question limit of '{user_count_limit}' per day."
            if serverfailcondition:
                faildescription = f"The server reached the daily question limit of '{server_count_limit} per day."
            failconditions = userfailcondition or serverfailcondition
            # Check if the user or server has reached the question limit
            if failconditions:
                await message.channel.send(
                    embed=discord.Embed(
                        type="rich",
                        title="Question limit reached",
                        description=faildescription,
                        color=discord.Colour.red(),
                    )
                )
                return

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

# Define the loop
@tasks.loop(hours=24)
async def reset_question_counts():
    global user_question_count, server_question_count
    user_question_count = {}
    server_question_count = {}
    print("Question counts reset at", datetime.datetime.now())

# Schedule the loop to start at the next midnight
@reset_question_counts.before_loop
async def before_reset_question_counts():
    now = datetime.datetime.now()
    midnight = now.replace(hour=0, minute=0, second=0, microsecond=0) + datetime.timedelta(days=1)
    time_until_midnight = midnight - now
    await asyncio.sleep(time_until_midnight.total_seconds())

# Start the loop
reset_question_counts.start()

try:
    client.run(DISCORD_BOT_APP_TOKEN)
except Exception as e:
    print(f"Error while running the bot: {e}")
