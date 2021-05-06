# Sven Discord Audio Bot

[![Codeac](https://static.codeac.io/badges/2-175096899.svg "Codeac")](https://app.codeac.io/github/lariskovski/sven-bot)

![skeleton](https://steamuserimages-a.akamaihd.net/ugc/172666989175739045/32D63249F0C0F276197D2576C86A081AB2061DD9/)

Simple yet fun Python bot for Discord servers. Allows the server participants to give a command that plays one of the audio files in the `audio` dir. Inspired by awesome [Sven Co-op](https://store.steampowered.com/app/225840/Sven_Coop/) latam servers that had a similiar mechanism.

## Technologies

- Python3

- Docker

- Github Actions

## Requirements

- Create a bot application on [Discord's developers portal](https://discord.com/developers/applications)

- Set the API_TOKEN env var from the Discord Application bot

- Install Docker

## Local Test

Build the image and run locally using the Makefile:

~~~~
make
~~~~

Opitionally, build, test and run separetely:

~~~~
make build
make test
make run
~~~~

Finally, clean everything with:

~~~~
make clean
~~~~

## Sources

[Github Actions and Docker](https://docs.docker.com/ci-cd/github-actions/)