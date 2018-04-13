# Twitch Clip Downloader

## What it is?

Twitch Clip Downloader is a simple python script to download automatically top clips of a game on Twitch (only selected language).

## Settings 

You MUST add a settings.py file to the root of the project to run the tool. This file must contain this variables (all strings, except LANGS):

- CLIENTID: Your twitch app client_id. More info https://blog.twitch.tv/client-id-required-for-kraken-api-calls-afbb8e95f843
- BASEDIR: The base directory where you want to download your files.
- GAME: The clips game.
- PERIOD: The lifetime of the clips.
- LIMIT: The number of clips you want obtain.
- LANGS: List of languages you wanna search. Each language implies one iteration of the tool.

## What else?

HAVE FUN :)
