import discord
from discord.ext import commands


class AdminTools(commands.Cog):
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
    bot.add_cog(AdminTools(bot))
