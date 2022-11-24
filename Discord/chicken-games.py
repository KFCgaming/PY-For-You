##Requirement package

import discord
from discord.ext import commands
import random

##Chicken list - I put 2 Chicken so that the probability of finding a bone is a little lower

ChickenGame = ["|| 🍗 ||","|| 🦴 ||","|| 🍗 ||","|| 🍗 ||"]

##Bot Config

prefix = ","

intents = discord.Intents.all()
intents.members = True
intents.presences = True
bot = commands.Bot(prefix, intents=intents)

## Chicken Command

@bot.command()
async def chicken(ctx):
    await ctx.send(random.choice(ChickenGame) + random.choice(ChickenGame) + random.choice(ChickenGame) + random.choice(ChickenGame) + random.choice(ChickenGame) + "\n" + random.choice(ChickenGame) + random.choice(ChickenGame) + random.choice(ChickenGame) + random.choice(ChickenGame) + random.choice(ChickenGame) +  "\n" + random.choice(ChickenGame) + random.choice(ChickenGame) + random.choice(ChickenGame) + random.choice(ChickenGame) + random.choice(ChickenGame) + "\n" + random.choice(ChickenGame) + random.choice(ChickenGame) + random.choice(ChickenGame) + random.choice(ChickenGame) + random.choice(ChickenGame) + "\n" + random.choice(ChickenGame) + random.choice(ChickenGame) + random.choice(ChickenGame) + random.choice(ChickenGame) + random.choice(ChickenGame))

## Replace TOKEN to your bot Token

bot.run("TOKEN")
