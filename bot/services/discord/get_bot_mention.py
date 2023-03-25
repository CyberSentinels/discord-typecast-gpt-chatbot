class UnknownBotMention:
    def __init__(self):
        self.name = "UNKNOWN_BOT_NAME"


def get_bot_mention(mentions):
    for mention in mentions:
        if mention.bot:
            return mention
    return UnknownBotMention()
