import discord
from discord.ext import commands
# import asyncio
from itertools import cycle
import youtube_dl

damn_son = 'https://www.youtube.com/watch?v=z8RkR4rd7dM'

# token da api
TOKEN = ''

# prefixo antes dos comandos
client = commands.Bot(command_prefix = '.')

# muda status de jogo do bot
# games = ['Fortnite', 'Grand Theft Auto V', 'CS:GO', 'Team Fortress 2']
# async def change_status():
# 	await client.wait_until_ready()
# 	status = cycle(games)

# 	while not client.is_closed:
# 		current_status = next(status)
# 		await client.change_presence(game=discord.Game(name=current_status))
# 		await asyncio.sleep(1200)

# confirma que esta rodando o bot
@client.event
async def on_ready():
	print("weeeeee!!")

# @client.command(pass_context=True)
# async def join(ctx):
# 	author = ctx.message.author
# 	channel = author.voice_channel
# 	await client.join_voice_channel(channel)
# 	# channel = ctx.message.author.voice.voice_channel
# 	# await client.join_voice_channel(channel)

# @client.command(pass_context=True)
# async def leave(ctx):
# 	server = ctx.message.server
# 	voice_client = client.voice_client_in(server)
# 	await voice_client.disconnect()

# @client.command()
# async def damnson():
# 	await client.say('damn???')

# @client.command(pass_context=True)
# async def damnson(ctx):
# 	server = ctx.message.server
# 	#voice = await client.join_voice_channel(server)
# 	voice_client = client.voice_client_in(server)
# 	player = await voice_client.create_ytdl_player(damn_son)
# 	#players[server.id] = player
# 	player.start()

@client.command(pass_context=True)
async def ping(ctx):
	ping_ = client.latency
	ping = round(ping_ * 1000)
	await ctx.channel.send(f"My ping is {ping}ms")

# @client.event
# async def on_member_join():
# 	pass

# client.loop.create_task(change_status())
client.run(TOKEN)

