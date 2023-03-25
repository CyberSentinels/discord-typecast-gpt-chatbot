# Use an official Python runtime as a parent image
FROM python:3.11.2-bullseye

LABEL org.opencontainers.image.source="https://github.com/CyberSentinels/discord-typecast-gpt-chatbot"
LABEL org.opencontainers.image.description="A Typecasted Chatbot for Discord Powered by ChatGPT and OpenAI API Calls."
LABEL org.opencontainers.image.authors="simeononsecurity"

# Set the working directory to /app
WORKDIR /

# Copy the current directory contents into the container at /
COPY . /

# Update packages and install required system dependencies
RUN apt-get update && \
    apt-get -y full-upgrade && \
    apt-get install -y locales python3-setuptools python3-dev python3-pip build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget libbz2-dev inetutils-ping gcc libpq-dev python3-venv python3-wheel python3-httptools

# Set environment variables for the desired locale
ENV LANG=en_US.UTF-8
ENV LANGUAGE=en_US:en
ENV LC_ALL=en_US.UTF-8

# Create a virtual environment and activate it
RUN python -m venv myenv
ENV PATH="/myenv/bin:${PATH}"

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Set the environment variable for the bot token
ENV DISCORD_BOT_APP_TOKEN=${DISCORD_BOT_APP_TOKEN}
ENV OPENAI_API_KEY=${OPENAI_API_KEY}

# Run app.py when the container launches
CMD ["python", "./bot/main.py"]
