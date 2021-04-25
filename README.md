# Sven Discord Audio Bot

![skeleton](https://steamuserimages-a.akamaihd.net/ugc/172666989175739045/32D63249F0C0F276197D2576C86A081AB2061DD9/)

Inspired on the Sven's server bot.

## Requirements

- Create a bot application on [Discord's developers portal](https://discord.com/developers/applications)

- Install Docker

## Run the bot locally

~~~~
docker build -t discord-bot  .
docker run -ti --env API_TOKEN=XXXXXXX discord-bot
~~~~
