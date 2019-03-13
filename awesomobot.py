import discord
from discord.ext import commands
import asyncio
from itertools import cycle
#import youtube_dl

# token da api
#TOKEN = 'NTU0Nzg2NjE5OTMzMzI3Mzgy.D2htGQ.0OW_Ns-CU2G8SKVWtrNIzHfk0Jg' ANTIGO
TOKEN= 'NTU1MTY3NjM5Mjc0NzgyNzMw.D2nPxw.hVd1N4jIezR0efXj8q9Tx8e_Uuw'

# prefixo antes dos comandos
client = commands.Bot(command_prefix = '.')
client.remove_command('help')

# muda status de jogo do bot
games = ['Fortnite', 'Grand Theft Auto V', 'CS:GO', 'Team Fortress 2']
async def change_status():
	await client.wait_until_ready()
	status = cycle(games)

	while not client.is_closed:
		current_status = next(status)
		await client.change_presence(game=discord.Game(name=current_status))
		await asyncio.sleep(600)

# confirma que esta rodando o bot
@client.event
async def on_ready():
	print("Beep beep beep[...]")

# JOINA E SAI DO CANAL DE VOZ
@client.command(pass_context=True)
async def join(ctx):
	author = ctx.message.author
	channel = author.voice_channel
	print(channel)
	await client.join_voice_channel(channel)

@client.command(pass_context=True)
async def leave(ctx):
	server = ctx.message.server
	voice_client = client.voice_client_in(server)
	await voice_client.disconnect()


""" ========================== COMANDOS DE VOZ ============================="""

@client.command()
async def help():
	await client.say("""
		Lista de comandos:
		.gatinho
		.nope
		.tf
		.sefodeu
		.alert
		.damnson
		.confirmed
		.sonic
		.mlg
		.csgo
		.pqp
		.mamamia""")

@client.command(pass_context=True)
async def damnson(ctx):
	server = ctx.message.server
	voice_client = client.voice_client_in(server)
	player = voice_client.create_ffmpeg_player('audio/damnson.mp3')
	player.start()

@client.command(pass_context=True)
async def tf(ctx):
	server = ctx.message.server
	voice_client = client.voice_client_in(server)
	player = voice_client.create_ffmpeg_player('audio/tf.mp3')
	player.start()

@client.command(pass_context=True)
async def pqp(ctx):
	server = ctx.message.server
	voice_client = client.voice_client_in(server)
	player = voice_client.create_ffmpeg_player('audio/pqp.mp3')
	player.start()


@client.command(pass_context=True)
async def sefodeu(ctx):
	server = ctx.message.server
	voice_client = client.voice_client_in(server)
	player = voice_client.create_ffmpeg_player('audio/sefodeu.mp3')
	player.start()

@client.command(pass_context=True)
async def sonic(ctx):
	server = ctx.message.server
	voice_client = client.voice_client_in(server)
	player = voice_client.create_ffmpeg_player('audio/sonic.mp3')
	player.start()

@client.command(pass_context=True)
async def mlg(ctx):
	server = ctx.message.server
	voice_client = client.voice_client_in(server)
	player = voice_client.create_ffmpeg_player('audio/mlg.mp3')
	player.start()


@client.command(pass_context=True)
async def nope(ctx):
	server = ctx.message.server
	voice_client = client.voice_client_in(server)
	player = voice_client.create_ffmpeg_player('audio/nope.mp3')
	player.start()

@client.command(pass_context=True)
async def confirmed(ctx):
	server = ctx.message.server
	voice_client = client.voice_client_in(server)
	player = voice_client.create_ffmpeg_player('audio/confirmed.mp3')
	player.start()

@client.command(pass_context=True)
async def alert(ctx):
	server = ctx.message.server
	voice_client = client.voice_client_in(server)
	player = voice_client.create_ffmpeg_player('audio/alert.mp3')
	player.start()

@client.command(pass_context=True)
async def csgo(ctx):
	server = ctx.message.server
	voice_client = client.voice_client_in(server)
	player = voice_client.create_ffmpeg_player('audio/csgo.mp3')
	player.start()


@client.command(pass_context=True)
async def mamamia(ctx):
	server = ctx.message.server
	voice_client = client.voice_client_in(server)
	player = voice_client.create_ffmpeg_player('audio/mamamia.mp3')
	player.start()

@client.command(pass_context=True)
async def gatinho(ctx):
	server = ctx.message.server
	voice_client = client.voice_client_in(server)
	player = voice_client.create_ffmpeg_player('audio/gatinho.mp3')
	player.start()

client.loop.create_task(change_status())
client.run(TOKEN)

