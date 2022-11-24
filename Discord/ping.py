##Requirement package

import discord
from discord.ext import commands
import random

##Bot Config

prefix = ","

intents = discord.Intents.all()
intents.members = True
intents.presences = True
bot = commands.Bot(prefix, intents=intents)

## Ping Command

@bot.command()
async def ping(ctx):
    embed=discord.Embed(title="Ping", description=f"{round(bot.latency * 1000 )} ms", color=0x0091ff)
    await ctx.send(embed=embed)
    
## Replace TOKEN to your bot Token

bot.run("TOKEN")
