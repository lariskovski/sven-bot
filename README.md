# Sven Discord Audio Bot

[![Codeac](https://static.codeac.io/badges/2-175096899.svg "Codeac")](https://app.codeac.io/github/lariskovski/sven-bot)

[![Build Status](https://dev.azure.com/larissaporto/devops/_apis/build/status/lariskovski.sven-bot?branchName=master)](https://dev.azure.com/larissaporto/devops/_build/latest?definitionId=2&branchName=master)

![skeleton](https://steamuserimages-a.akamaihd.net/ugc/172666989175739045/32D63249F0C0F276197D2576C86A081AB2061DD9/)

Inspired on the Sven's server bot.

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
