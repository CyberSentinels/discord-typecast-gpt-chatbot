from services.datetime.now import now_ca, now_us
from services.discord.repl_mention_ids_with_usernames import repl_mention_ids_with_usernames
from services.discord.get_bot_mention import get_bot_mention
from services.openai.get_system_content import get_system_content
from services.openai.get_user_content import get_user_content
from services.openai.batch_and_format_for_discord import batch_and_format_for_discord
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
    date = now_us()
    date_toronto = now_ca()
    system_content = get_system_content()
    user_content = get_user_content(
        discord_msg_content_with_usernames,
        discord_msg_author_name,
        discord_bot_name,
        date,
        date_toronto,
    )
    chatml_messages = create_chatml_messages(system_content, user_content)
    openai = create_openai_client()

    # try chat completion request
    try:
        chat_completion_response = get_chat_completion(openai, chatml_messages)
    except Exception as e:
        raise e
    
    # take only the part of the response we care about
    content = chat_completion_response.choices[0].message.content.strip()

    # update current chat and chat history
    user_content.append_to_current_chat(content)
    user_content.append_to_chat_history(content)

    # batch responses for discord
    responses = batch_and_format_for_discord(content)

    while responses:
        discord_response_content = responses.pop(0).strip()
        debug(system_content, user_content, discord_response_content)
        await message.channel.send(content)

    # send response to discord channel
    await message.channel.send(content=content)


def debug(system_content, user_content, discord_response_content):
    print('DEBUG START....')
    print('')
    print('---------------------------')
    print('SYSTEM CONTENT:')
    print('---------------------------')
    print(system_content.as_str())
    print('')
    print('---------------------------')
    print('USER CONTENT:')
    print('---------------------------')
    print(user_content.as_str())
    print('')
    print('---------------------------')
    print('CHAT HISTORY LENGTH:')
    print('---------------------------')
    print(len(user_content.get_chat_history()))
    print('')
    print('---------------------------')
    print('TIME UNTIL CHAT HISTORY EXPIRES:')
    print('---------------------------')
    print(user_content.get_time_until_chat_history_expires())
    print('')
    print('---------------------------')
    print('CHAT COMPLETION RESPONSE:')
    print('---------------------------')
    print(discord_response_content)
    print('')
    print('---------------------------')
    print('...DEBUG END')
    print('')
