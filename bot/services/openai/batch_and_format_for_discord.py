def batch_and_format_for_discord(response):
    # precondition: response is chat_completion_response.choices[0].message.content.strip()

    # Discord character limit is 2000
    # We'll batch responses into multiple messages if we go over
    character_limit = 2000
    lines = response.strip().split('\n')
    responses = ['']
    char_count = 0
    in_code = False
    while lines:
        line = lines.pop(0)
        # character_limit - 3 because of code formatting
        if char_count + len(line) + 1 > (character_limit - 3):
            if in_code:
                responses[-1] += '```'
                responses.append('```')
                char_count = 3
            else:
                responses.append('')
                char_count = 0
        responses[-1] = responses[-1] or ''
        responses[-1] += line + '\n'
        # Trim line to make sure it fits
        responses[-1] = responses[-1][:character_limit - 3]
        char_count += len(line) + 1
        if line.startswith('```'):
            in_code = not in_code

    # Close the last code block if necessary
    if in_code:
        responses[-1] += '```'

    # Filter out empty response lines
    responses = list(filter(lambda response: bool(response), responses))
    return responses
