from discord.ext import commands
from itertools import cycle
from os import walk
import discord
import asyncio

# token da api
TOKEN = 'NTU1MTY3NjM5Mjc0NzgyNzMw.D2ptxQ.ej_YWc2cD2yH5gFyJyTfcmIG7nU'

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
for (dirpath, dirnames, filenames) in walk('audio'):
	files = filenames
audios = []
for audio in files:
	audio = '.' + audio
	audios.append(audio.replace('.mp3',''))
audios = '\n'.join(audios)

@client.command()
async def help():
	await client.say(audios)

@client.command(pass_context=True)
async def damnson(ctx):
	server = ctx.message.server
	voice_client = client.voice_client_in(server)
	player = voice_client.create_ffmpeg_player('audio/damnson.mp3')
	player.start()

@client.command(pass_context=True)
async def pqp(ctx):
	server = ctx.message.server
	voice_client = client.voice_client_in(server)
	player = voice_client.create_ffmpeg_player('audio/pqp.mp3')
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
async def alert(ctx):
	server = ctx.message.server
	voice_client = client.voice_client_in(server)
	player = voice_client.create_ffmpeg_player('audio/alert.mp3')
	player.start()

@client.command(pass_context=True)
async def mamamia(ctx):
	server = ctx.message.server
	voice_client = client.voice_client_in(server)
	player = voice_client.create_ffmpeg_player('audio/mamamia.mp3')
	player.start()
	
@client.command(pass_context=True)
async def naruto(ctx):
	server = ctx.message.server
	voice_client = client.voice_client_in(server)
	player = voice_client.create_ffmpeg_player('audio/naruto.mp3')
	player.start()

	
@client.command(pass_context=True)
async def berg(ctx):
	server = ctx.message.server
	voice_client = client.voice_client_in(server)
	player = voice_client.create_ffmpeg_player('audio/berg.mp3')
	player.start()

@client.command(pass_context=True)
async def fahur(ctx):
	server = ctx.message.server
	voice_client = client.voice_client_in(server)
	player = voice_client.create_ffmpeg_player('audio/fahur.mp3')
	player.start()
	
@client.command(pass_context=True)
async def cafe(ctx):
	server = ctx.message.server
	voice_client = client.voice_client_in(server)
	player = voice_client.create_ffmpeg_player('audio/cafe.mp3')
	player.start()

@client.command(pass_context=True)
async def coffee(ctx):
	server = ctx.message.server
	voice_client = client.voice_client_in(server)
	player = voice_client.create_ffmpeg_player('audio/coffee.mp3')
	player.start()
	
@client.command(pass_context=True)
async def lick(ctx):
	server = ctx.message.server
	voice_client = client.voice_client_in(server)
	player = voice_client.create_ffmpeg_player('audio/lick.mp3')
	player.start()
	
@client.command(pass_context=True)
async def stop(ctx):
	server = ctx.message.server
	voice_client = client.voice_client_in(server)
	player = voice_client.create_ffmpeg_player('audio/stop.mp3')
	player.start()
	
@client.command(pass_context=True)
async def quackjob(ctx):
	server = ctx.message.server
	voice_client = client.voice_client_in(server)
	player = voice_client.create_ffmpeg_player('audio/quackjob.mp3')
	player.start()
	
@client.command(pass_context=True)
async def sucks(ctx):
	server = ctx.message.server
	voice_client = client.voice_client_in(server)
	player = voice_client.create_ffmpeg_player('audio/sucks.mp3')
	player.start()
	
@client.command(pass_context=True)
async def epic(ctx):
	server = ctx.message.server
	voice_client = client.voice_client_in(server)
	player = voice_client.create_ffmpeg_player('audio/epic.mp3')
	player.start()
	
@client.command(pass_context=True)
async def meat(ctx):
	server = ctx.message.server
	voice_client = client.voice_client_in(server)
	player = voice_client.create_ffmpeg_player('audio/meat.mp3')
	player.start()
	
@client.command(pass_context=True)
async def term(ctx):
	server = ctx.message.server
	voice_client = client.voice_client_in(server)
	player = voice_client.create_ffmpeg_player('audio/term.mp3')
	player.start()
	
@client.command(pass_context=True)
async def stray(ctx):
	server = ctx.message.server
	voice_client = client.voice_client_in(server)
	player = voice_client.create_ffmpeg_player('audio/stray.mp3')
	player.start()
	
@client.command(pass_context=True)
async def ayuss(ctx):
	server = ctx.message.server
	voice_client = client.voice_client_in(server)
	player = voice_client.create_ffmpeg_player('audio/ayuss.mp3')
	player.start()

@client.command(pass_context=True)
async def monkeyman(ctx):
	server = ctx.message.server
	voice_client = client.voice_client_in(server)
	player = voice_client.create_ffmpeg_player('audio/monkeyman.mp3')
	player.start()

@client.command(pass_context=True)
async def sad(ctx):
	server = ctx.message.server
	voice_client = client.voice_client_in(server)
	player = voice_client.create_ffmpeg_player('audio/sad.mp3')
	player.start()
	
@client.command(pass_context=True)
async def rip(ctx):
	server = ctx.message.server
	voice_client = client.voice_client_in(server)
	player = voice_client.create_ffmpeg_player('audio/rip.mp3')
	player.start()
	
@client.command(pass_context=True)
async def ayuda(ctx):
	server = ctx.message.server
	voice_client = client.voice_client_in(server)
	player = voice_client.create_ffmpeg_player('audio/ayuda.mp3')
	player.start()

@client.command(pass_context=True)
async def jaja(ctx):
	server = ctx.message.server
	voice_client = client.voice_client_in(server)
	player = voice_client.create_ffmpeg_player('audio/jaja.mp3')
	player.start()

@client.command(pass_context=True)
async def no(ctx):
	server = ctx.message.server
	voice_client = client.voice_client_in(server)
	player = voice_client.create_ffmpeg_player('audio/no.mp3')
	player.start()

@client.command(pass_context=True)
async def puto(ctx):
	server = ctx.message.server
	voice_client = client.voice_client_in(server)
	player = voice_client.create_ffmpeg_player('audio/puto.mp3')
	player.start()

@client.command(pass_context=True)
async def gta(ctx):
	server = ctx.message.server
	voice_client = client.voice_client_in(server)
	player = voice_client.create_ffmpeg_player('audio/gta.mp3')
	player.start()

@client.command(pass_context=True)
async def mentir(ctx):
	server = ctx.message.server
	voice_client = client.voice_client_in(server)
	player = voice_client.create_ffmpeg_player('audio/mentir.mp3')
	player.start()

@client.command(pass_context=True)
async def riso(ctx):
	server = ctx.message.server
	voice_client = client.voice_client_in(server)
	player = voice_client.create_ffmpeg_player('audio/riso.mp3')
	player.start()

@client.command(pass_context=True)
async def careless(ctx):
	server = ctx.message.server
	voice_client = client.voice_client_in(server)
	player = voice_client.create_ffmpeg_player('audio/careless.mp3')
	player.start()

@client.command(pass_context=True)
async def ohyeah(ctx):
	server = ctx.message.server
	voice_client = client.voice_client_in(server)
	player = voice_client.create_ffmpeg_player('audio/ohyeah.mp3')
	player.start()

@client.command(pass_context=True)
async def ayudenme(ctx):
	server = ctx.message.server
	voice_client = client.voice_client_in(server)
	player = voice_client.create_ffmpeg_player('audio/ayudenme.mp3')
	player.start()

@client.command(pass_context=True)
async def pig(ctx):
	server = ctx.message.server
	voice_client = client.voice_client_in(server)
	player = voice_client.create_ffmpeg_player('audio/pig.mp3')
	player.start()

@client.command(pass_context=True)
async def boo(ctx):
	server = ctx.message.server
	voice_client = client.voice_client_in(server)
	player = voice_client.create_ffmpeg_player('audio/boo.mp3')
	player.start()
	
@client.command(pass_context=True)
async def pepp(ctx):
	server = ctx.message.server
	voice_client = client.voice_client_in(server)
	player = voice_client.create_ffmpeg_player('audio/pepp.mp3')
	player.start()

@client.command(pass_context=True)
async def jestah(ctx):
	server = ctx.message.server
	voice_client = client.voice_client_in(server)
	player = voice_client.create_ffmpeg_player('audio/jestah.mp3')
	player.start()

@client.command(pass_context=True)
async def nu(ctx):
	server = ctx.message.server
	voice_client = client.voice_client_in(server)
	player = voice_client.create_ffmpeg_player('audio/nu.mp3')
	player.start()

@client.command(pass_context=True)
async def dansa(ctx):
	server = ctx.message.server
	voice_client = client.voice_client_in(server)
	player = voice_client.create_ffmpeg_player('audio/dansa.mp3')
	player.start()

@client.command(pass_context=True)
async def cont(ctx):
	server = ctx.message.server
	voice_client = client.voice_client_in(server)
	player = voice_client.create_ffmpeg_player('audio/cont.mp3')
	player.start()

@client.command(pass_context=True)
async def dolph(ctx):
	server = ctx.message.server
	voice_client = client.voice_client_in(server)
	player = voice_client.create_ffmpeg_player('audio/dolph.mp3')
	player.start()

@client.command(pass_context=True)
async def reprov(ctx):
	server = ctx.message.server
	voice_client = client.voice_client_in(server)
	player = voice_client.create_ffmpeg_player('audio/reprov.mp3')
	player.start()

@client.command(pass_context=True)
async def dentad(ctx):
	server = ctx.message.server
	voice_client = client.voice_client_in(server)
	player = voice_client.create_ffmpeg_player('audio/dentad.mp3')
	player.start()

@client.command(pass_context=True)
async def traiu(ctx):
	server = ctx.message.server
	voice_client = client.voice_client_in(server)
	player = voice_client.create_ffmpeg_player('audio/traiu.mp3')
	player.start()

@client.command(pass_context=True)
async def serj(ctx):
	server = ctx.message.server
	voice_client = client.voice_client_in(server)
	player = voice_client.create_ffmpeg_player('audio/serj.mp3')
	player.start()

@client.command(pass_context=True)
async def parab(ctx):
	server = ctx.message.server
	voice_client = client.voice_client_in(server)
	player = voice_client.create_ffmpeg_player('audio/parab.mp3')
	player.start()

@client.command(pass_context=True)
async def bilu(ctx):
	server = ctx.message.server
	voice_client = client.voice_client_in(server)
	player = voice_client.create_ffmpeg_player('audio/bilu.mp3')
	player.start()

@client.command(pass_context=True)
async def jess(ctx):
	server = ctx.message.server
	voice_client = client.voice_client_in(server)
	player = voice_client.create_ffmpeg_player('audio/jess.mp3')
	player.start()

@client.command(pass_context=True)
async def chav(ctx):
	server = ctx.message.server
	voice_client = client.voice_client_in(server)
	player = voice_client.create_ffmpeg_player('audio/chav.mp3')
	player.start()

@client.command(pass_context=True)
async def caluni(ctx):
	server = ctx.message.server
	voice_client = client.voice_client_in(server)
	player = voice_client.create_ffmpeg_player('audio/caluni.mp3')
	player.start()

@client.command(pass_context=True)
async def some(ctx):
	server = ctx.message.server
	voice_client = client.voice_client_in(server)
	player = voice_client.create_ffmpeg_player('audio/some.mp3')
	player.start()
	
@client.command(pass_context=True)
async def piss(ctx):
	server = ctx.message.server
	voice_client = client.voice_client_in(server)
	player = voice_client.create_ffmpeg_player('audio/piss.mp3')
	player.start()
@client.command(pass_context=True)
async def nikolai(ctx):
	server = ctx.message.server
	voice_client = client.voice_client_in(server)
	player = voice_client.create_ffmpeg_player('audio/nikolai.mp3')
	player.start()

@client.command(pass_context=True)
async def wat(ctx):
	server = ctx.message.server
	voice_client = client.voice_client_in(server)
	player = voice_client.create_ffmpeg_player('audio/wat.mp3')
	player.start()

@client.command(pass_context=True)
async def blyat(ctx):
	server = ctx.message.server
	voice_client = client.voice_client_in(server)
	player = voice_client.create_ffmpeg_player('audio/blyat.mp3')
	player.start()

@client.command(pass_context=True)
async def opin(ctx):
	server = ctx.message.server
	voice_client = client.voice_client_in(server)
	player = voice_client.create_ffmpeg_player('audio/opin.mp3')
	player.start()
	
@client.command(pass_context=True)
async def bor(ctx):
	server = ctx.message.server
	voice_client = client.voice_client_in(server)
	player = voice_client.create_ffmpeg_player('audio/bor.mp3')
	player.start()

@client.command(pass_context=True)
async def boi(ctx):
	server = ctx.message.server
	voice_client = client.voice_client_in(server)
	player = voice_client.create_ffmpeg_player('audio/boi.mp3')
	player.start()

@client.command(pass_context=True)
async def getout(ctx):
	server = ctx.message.server
	voice_client = client.voice_client_in(server)
	player = voice_client.create_ffmpeg_player('audio/getout.mp3')
	player.start()
	
@client.command(pass_context=True)
async def aaah(ctx):
	server = ctx.message.server
	voice_client = client.voice_client_in(server)
	player = voice_client.create_ffmpeg_player('audio/aaah.mp3')
	player.start()
		
client.loop.create_task(change_status())
client.run(TOKEN)
