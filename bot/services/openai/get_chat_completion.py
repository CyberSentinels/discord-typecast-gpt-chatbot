import time
from requests.exceptions import RequestException


def create_chatml_messages(system_content, user_content):
    chatml_messages = [
        {
            "role": "system",
            "content": system_content
        },
        {
            "role": "user",
            "content": user_content
        }
    ]
    return chatml_messages


def get_chat_completion(openai, chatml_messages):
    max_retries = 3
    delay = 5
    for retry in range(max_retries):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=chatml_messages,
                max_tokens=256,
                temperature=0.8,
                top_p=1,
                n=1,
                presence_penalty=0.2,
                frequency_penalty=0.2,
            )
            return response
        except RequestException as e:
            if retry == max_retries - 1:
                print("Maximum retries exceeded. Raising exception.")
                raise e
            print(f"Request failed. Retrying in {delay} seconds...")
            time.sleep(delay)
            delay += 10
    return None
