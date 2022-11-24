##Requirement package

import discord
from discord.ext import commands
import random

##Casino list

Casino = ["💎 ", "🍒 ", "7 "]

##Bot Config

prefix = ","

intents = discord.Intents.all()
intents.members = True
intents.presences = True
bot = commands.Bot(prefix, intents=intents)

## Casino Command

@bot.command()
async def casino(ctx):
    await ctx.send("Start of the machine... 🎰")
    await ctx.send("**" + random.choice(Casino) + random.choice(Casino) + random.choice(Casino) + "**")

## Replace TOKEN to your bot Token

bot.run("TOKEN")
