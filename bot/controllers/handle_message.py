import time
from services.datetime.now import now_ca, now_us
from services.discord.repl_mention_ids_with_usernames import repl_mention_ids_with_usernames
from services.discord.get_bot_mention import get_bot_mention
from services.openai.user_content.prefix_helpers.get_current_chat_prefix import get_current_chat_prefix
from services.openai.user_content.chat_history.get_chat_history import get_chat_history
from services.openai.get_system_content import get_system_content
from services.openai.user_content.get_user_content import get_user_content
from services.openai.batch_and_format_for_discord import batch_and_format_for_discord
from services.openai.get_chat_completion import create_chatml_messages, get_chat_completion
from services.openai.create_openai_client import create_openai_client


async def handle_message(message):
    # extract discord message data for openai chat completion
    orig_content = message.content
    mentions = message.mentions
    discord_bot_mention = get_bot_mention(mentions)
    discord_bot_name = discord_bot_mention.name
    discord_msg_author_name = message.author.name

    # transform discord message data for openai chat completion
    discord_msg_content_with_usernames = repl_mention_ids_with_usernames(
        orig_content,
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
    max_retries = 3
    delay = 5
    while True:
        try:
            chat_completion_response = get_chat_completion(
                openai, chatml_messages)
        except Exception as e:
            if max_retries == 0:
                print("Maximum retries exceeded. Raising exception.")
                raise e
            await message.channel.send(f"Request failed. Retrying in {delay} seconds...")
            time.sleep(delay)
            max_retries -= 1
            delay += 10

    # take only the part of the response we care about
    chatgpt_content = chat_completion_response.choices[0].message.content.strip(
    )

    # update chat history
    chat_history_for_this_user = get_chat_history(discord_msg_author_name)
    if (chat_history_for_this_user.get_time_until_expires() <= 0):
        chat_history_for_this_user.reset()
    if (chat_history_for_this_user.is_full()):
        chat_history_for_this_user.remove_old_entry()
    chat_prefix = get_current_chat_prefix(
        discord_msg_author_name,
        discord_bot_name,
        discord_msg_content_with_usernames,
        date
    )
    new_chat_entry = chat_prefix + chatgpt_content
    chat_history_for_this_user.append(new_chat_entry)

    # batch responses for discord
    responses = batch_and_format_for_discord(chatgpt_content)

    while responses:
        discord_response_content = responses.pop(0).strip()
        await message.channel.send(discord_response_content)
