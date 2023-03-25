import re

def repl_id_with_username(matched_id, msg_mentions):
    for mention in msg_mentions:
        if (str(mention.id) == str(matched_id)):
            return f'<@{mention.name}>'
    return f'<@:unknown>'


def repl_mention_ids_with_usernames(msg_content, msg_mentions):
    return re.sub(r'<@(\d+)>', lambda g: repl_id_with_username(g[1], msg_mentions), msg_content)

# run with pytest
class TestReplMentionIdsWithUsernames:
    class mention:
        def __init__(self, id, name):
            self.id = id
            self.name = name

    def test_no_mention_ids(self):
        msg_content = "Hello World"
        msg_mentions = []
        assert repl_mention_ids_with_usernames(
            msg_content, msg_mentions) == msg_content

    def test_no_matching_mention_ids(self):
        msg_content = "Hey <@1234>, how are you doing?"
        msg_mentions = []
        expected_output = "Hey <@:unknown>, how are you doing?"
        assert repl_mention_ids_with_usernames(
            msg_content, msg_mentions) == expected_output

    def test_matching_mention_ids(self):
        msg_content = "Hey <@1234>, how are you doing?"
        msg_mentions = [self.mention(id=1234, name="John")]
        expected_output = "Hey <@John>, how are you doing?"
        assert repl_mention_ids_with_usernames(
            msg_content, msg_mentions) == expected_output

    def test_multiple_mention_ids(self):
        msg_content = "Hello <@1234>, how are you doing? <@5678>"
        msg_mentions = [self.mention(
            id=1234, name="John"), self.mention(id=5678, name="Jane")]
        expected_output = "Hello <@John>, how are you doing? <@Jane>"
        assert repl_mention_ids_with_usernames(
            msg_content, msg_mentions) == expected_output

    def test_fake_mention_id(self):
        msg_content = "Hello <@1234>, how are you doing? <@abc>"
        msg_mentions = [self.mention(id=1234, name="John")]
        expected_output = "Hello <@John>, how are you doing? <@abc>"
        assert repl_mention_ids_with_usernames(
            msg_content, msg_mentions) == expected_output
