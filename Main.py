""" Cody Kenstler
Using discord.py: https://discordpy.readthedocs.io/en/rewrite/index.html
"""
import discord
import os
from discord.ext import commands
import Functions

# Sets what prefix triggers the bot commands
bot = commands.Bot(command_prefix='$')


# Announce successful connection to Discord
@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


# Announce successful disconnect from Discord servers
@bot.event
async def on_disconnect():
    print('We have logged out of Discord!')


""" While load, unload, and reload are admin functions, 
it's outside the admin class so that it can never be removed accidentally"""
# command allows user to load in new cogs after the bot is running
@bot.command()
@commands.has_permissions(manage_guild=True)
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')


# command allows user to unload in new cogs after the bot is running
@bot.command()
@commands.has_permissions(manage_guild=True)
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')


# Update a cog to it's newest version, if there is an error the bot will rollback
@bot.command()
@commands.has_permissions(manage_guild=True)
async def reload(ctx, extension):
    bot.reload_extension(f'cogs.{extension}')


# Load all cogs into bot
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(Functions.login())
