# compassionate conversationalist bot

## How to run the bot
To get started with running this repository, you need to perform the following steps:

1. Clone this repository and change into product root

```sh
git clone URL
cd repo_name
```
2. create an `.env` file in the project root (it will be `.gitignored` so you don't commit your code) and paste your discord bot token and openai token:

```sh
DISCORD_BOT_APP_TOKEN=PASTE_DISCORD_TOKEN_HERE
OPENAI_API_KEY=PASTE_OPENAI_API_TOKEN_HERE
```

3. Create a new virtual environment using `venv`:
```sh
python3 -m venv venv
```

4. Activate the virtual environment:
```sh
source venv/bin/activate
```

5. Install the dependencies listed in `requirements.txt`:
   
```sh
pip install -r requirements.txt
```

6. If you install new dependencies with `pip install`, be sure to regenerate requirements.txt with:

```sh
pip freeze > requirements.txt
```

### Architecture

```text
./
project root

bot/
discord bot's source

bot/main.py:
This is the main entry point for your application

bot/controllers/
This directory contains code that controls the main program and provides inputs into services

bot/services/
This directory contains code that do small, specific tasks

requirements.txt:
This file lists the dependencies required for your application to run

_misc/
example HTTP webserver written in python
```
