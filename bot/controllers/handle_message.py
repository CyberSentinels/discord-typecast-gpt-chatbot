from services.discord.get_bot_mention import get_bot_mention
from services.discord.repl_mention_ids_with_usernames import repl_mention_ids_with_usernames
from services.openai.get_chat_completion import create_chatml_messages, get_chat_completion
from services.openai.create_openai_client import create_openai_client


async def handle_message(message):
    # extract discord message data for openai chat completion
    content = message.content
    mentions = message.mentions
    discord_bot_mention = get_bot_mention(mentions)
    discord_bot_name = discord_bot_mention.name
    discord_msg_author_name = message.author.name

    # transform discord message data for openai chat completion
    discord_msg_content_with_usernames = repl_mention_ids_with_usernames(
        content,
        mentions
    )

    # construct chatml message data for openai chat completion, from discord message data
    chatml_messages = create_chatml_messages(
        discord_msg_content_with_usernames,
        discord_msg_author_name,
        discord_bot_name
    )

    # request chat completion data
    openai = create_openai_client()

    # construct discord channel message for response, from chat completion response
    try:
        chat_completion_response = await get_chat_completion(openai, chatml_messages)
    except Exception as e:
        raise e

    # chat_completion_response
    content = chat_completion_response.choices[0].message.content.strip(
    )

    # send response to discord channel
    await message.channel.send(content=content)
