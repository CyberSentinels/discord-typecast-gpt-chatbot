from services.openai.user_content.chat_history.get_examples import get_examples
from services.openai.user_content.prefix_helpers.get_assistant_prefix import get_assistant_prefix
from services.openai.user_content.prefix_helpers.get_user_prefix import get_user_prefix
from services.openai.user_content.prefix_helpers.get_current_chat_prefix import get_current_chat_prefix
from services.openai.user_content.get_context import get_context
from services.openai.user_content.chat_history.get_chat_history import get_chat_history


def get_user_content(
    discord_msg,
    discord_msg_author_name,
    discord_bot_name,
    date,
    date_toronto,
):
    user_prefix = get_user_prefix(date, discord_msg_author_name)
    assistant_prefix = get_assistant_prefix(date, discord_bot_name)
    return f"""{get_context(discord_bot_name, date)}
{get_examples(user_prefix, assistant_prefix, discord_msg_author_name, discord_bot_name, date_toronto)}
{get_chat_history(discord_msg_author_name)}
Current Chat:
{get_current_chat_prefix(user_prefix, assistant_prefix, discord_msg, date)}
"""
