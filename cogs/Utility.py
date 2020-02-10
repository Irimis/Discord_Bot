"""Utility functions such as: Giving the bots link, checking ping, users time of creation"""

import discord
from discord.ext import commands


class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # creates a invite link for the bot so users can add it to their own servers
    @commands.command()
    async def inviteLink(self, ctx):
        invite = discord.utils.oauth_url('487152144110190612')
        await ctx.send("You can add me to your server by using " + invite)

    # tells the user how old their account is
    @commands.command()
    async def howOld(self, ctx):
        userID = ctx.message.author.id
        accAge = discord.utils.snowflake_time(userID)
        await ctx.send("Your account was created on " + accAge.strftime("%m/%d/%Y, %H:%M:%S") + " UTC")

    # Bot will give it's ping in ms
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(self.bot.latency * 1000 )}ms')


def setup(bot):
    bot.add_cog(Utility(bot))