from services.openai.user_content.prefix_helpers.get_assistant_prefix import get_assistant_prefix
from services.openai.user_content.prefix_helpers.get_user_prefix import get_user_prefix


def get_current_chat_prefix(discord_msg_author_name, discord_bot_name, discord_msg, date):
    user_prefix = get_user_prefix(date, discord_msg_author_name)
    assistant_prefix = get_assistant_prefix(date, discord_bot_name)
    return f"""{user_prefix}: {discord_msg}
{assistant_prefix}:"""
