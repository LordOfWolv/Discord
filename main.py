import random
import discord
from discord.ext import commands
from bot_logic import gen_pass, gen_coin

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hello! Im live in Russia {bot.user}!')

@bot.command()
async def helpp(ctx):
    await ctx.send(f'Go to my telegram channel to learn more about the functions and commands of the bot')

@bot.command()
async def password(ctx):
    await ctx.send(gen_pass())

@bot.command()
async def coin(ctx):
    await ctx.send(gen_coin())




bot.run('MTE1MjkwODQyMzIzNTY0OTYwNw.G93C3V.5gAt4yY9GeL5tcrWXnO6ZoVBW_u6_oelBQOpO8')
