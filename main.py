import discord
from discord.ext import commands
from os import getenv, walk
from time import sleep

TOKEN = getenv('API_TOKEN')
client = commands.Bot(command_prefix = '.')

# Get all file names from audio directory
for (dirpath, dirnames, filenames) in walk('audio'):
	files = filenames
audios = []
for audio in files:
	audios.append(audio.replace('.mp3',''))
audios = ', '.join(audios)

@client.command(name="audios", brief='Lists all audios available', pass_context=True)
async def audiosAvailable(ctx):
    await ctx.send(audios)

@client.command(brief='This command plus an audio name, plays it', name="play")
async def play(ctx, *, text):
    # Gets voice channel of message author
    voice_channel = ctx.author.voice.channel
    message = text
    channel = None
    if voice_channel != None:
        channel = voice_channel.name
        vc = await voice_channel.connect()
        vc.play(discord.FFmpegPCMAudio(source=f"audio/{message}.mp3"))
        # Sleep while audio is playing.
        while vc.is_playing():
            sleep(.1)
        await vc.disconnect()
    else:
        await ctx.send(str(ctx.author.name) + "is not in a channel.")
    # Delete command after the audio is done playing.
    await ctx.message.delete()

# Outputs on server terminal ready message
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

client.run(TOKEN)