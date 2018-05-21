#Yuri bot for YuriProtectionAgency.
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

bot = commands.Bot(command_prefix='!y ')

@bot.event
async def on_ready():
    print ("Bot online.")
    await bot.change_presence(game=discord.Game(name="with MC's pen"))

@bot.command(pass_context=True)
async def nirvana(ctx):
    await bot.say("https://www.youtube.com/watch?v=NJqQf5DObtY")

@bot.command(pass_context=True)
async def iloveyou(ctx):
    await bot.say("https://i.redd.it/qs3odxjgi3vz.png")

@bot.command(pass_context=True)
async def porn(ctx):
    await bot.say("https://cdn.discordapp.com/attachments/437011976351383557/437012039798620180/hellyeahilikePORN.png")

@bot.command(pass_context=True)
async def lost(ctx):
    await bot.say("https://youtu.be/xj7RMPM3A2c")

@bot.command(pass_context=True)
async def thick(ctx):
    await bot.say("https://cdn.discordapp.com/attachments/437011976351383557/437012185441370133/shitmeme.png")

@bot.command(pass_context=True)
async def soldier(ctx):
    await bot.say("Welcome to the soldier side")
    await bot.say("Where there's no one here but me")
    await bot.say("People all grow up to die")
    await bot.say("There is no one here but me.")

@bot.command(pass_context=True)
async def hate(ctx):
    await bot.say("https://i.redd.it/jgrci9wr4pq01.png")

@bot.command(pass_context=True)
async def ralf(ctx):
    await bot.say("https://cdn.discordapp.com/attachments/437011976351383557/437012834522497033/image.png")

@bot.command(pass_context=True)
async def chibi(ctx):
    await bot.say("https://i.redd.it/uk5x9pftdlm01.png")

@bot.command(pass_context=True)
async def lewd(ctx):
    await bot.say("https://cdn.discordapp.com/attachments/436743371873058817/436998735269068801/t4fnga1356501.png")

bot.run("NDM2ODYyNjM4Nzk0OTk3NzYw.DbvdQg.Fasfi5KvhTZnJkhm2uCQOsMY54c")