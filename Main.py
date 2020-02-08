""" Cody Kenstler
Using discord.py: https://discordpy.readthedocs.io/en/rewrite/index.html
"""
import discord
import os
from discord.ext import commands
import Functions

# sets what prefix triggers the bot commands
bot = commands.Bot(command_prefix='$')


# Announce successful connection to Discord
@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


# Announce successful disconnect from Discord servers
@bot.event
async def on_disconnect():
    print('We have logged out of Discord!')


# Load all cogs into bot
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(Functions.login())
