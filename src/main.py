# This example requires the 'message_content' privileged intents

import os
import logging

import discord
from discord.ext import commands
from dotenv import load_dotenv

log = logging.getLogger("main")
load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
TOKEN = os.getenv("DISCORD_TOKEN")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@bot.command()
async def hello(ctx):
    await ctx.send("Choo choo! 🚅")


bot.run(TOKEN)