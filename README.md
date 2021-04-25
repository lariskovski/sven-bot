# Discord Audio Bot

Inspired on the Sven server's bot.

## Requirements

- Create a bot application on [Discord's developers portal] (https://discord.com/developers/applications)

- Install Docker

## Run the bot locally

~~~~
docker build -t discord-bot  .
docker run -ti --env API_TOKEN=XXXXXXX discord-bot
~~~~
