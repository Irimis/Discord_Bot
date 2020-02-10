"""This class will be used for functions that are for: server admins, moderators, or the bot owner themselves
to add or remove functionality or disable the bot"""

import discord
from discord.ext import commands


class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Shutoff bot and end program if the person invoking the command is the bot's owner
    @commands.command()
    @commands.is_owner()
    async def logout(self, ctx):
        await ctx.send('Bye!')
        await self.bot.logout()


# sets up cog to be used by bot in main
def setup(bot):
    bot.add_cog(Admin(bot))
