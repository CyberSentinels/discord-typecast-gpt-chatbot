import time

TTL = 600
MAX_LENGTH = 5


class ChatHistory:
    def __init__(self, username):
        self.username = username
        self.chats = []
        self.birth_time = time.time()

    def reset(self):
        self.chats = []
        self.birth_time = time.time()

    def append(self, value):
        print('appending:')
        print(value)
        print('to:')
        print(self.chats)
        print('for:')
        print(self.username)
        self.chats.append(value)

    def remove_old_entry(self):
        self.chats.pop(0)

    def get_time_until_expires(self):
        return TTL - (time.time() - self.birth_time)

    def is_full(self):
        return len(self.chats) == MAX_LENGTH

    def __str__(self):
        return "\n".join(self.chats)


chat_histories = {}  # global singleton


def get_chat_history(username):
    global chat_histories
    if (username in chat_histories):
        return chat_histories[username]
    else:
        chat_histories[username] = ChatHistory(username)
        return chat_histories[username]
