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
    except Exception as e:
        print("error in get_chat_completion")
        raise e
