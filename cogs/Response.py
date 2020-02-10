"""The function of this will serve for basic chat responses such as: greeting new members,
responding to basic pings, anything using simple text commands"""

import discord
from discord.ext import commands


class Response(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Welcomes new member to group
    @commands.Cog.listener()
    async def on_member_join(self,member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send('Welcome {0.mention}.'.format(member))

    # Repeats what user said
    @commands.command()
    async def repeat(self, ctx, arg):
        await ctx.send(arg)

    # Says how many different arguments the user sent
    @commands.command()
    async def test(self, ctx, *args):
        await ctx.send('{} arguments: {}'.format(len(args), ', '.join(args)))

# sets up cog to allow it to be used by the bot in main
def setup(bot):
    bot.add_cog(Response(bot))
