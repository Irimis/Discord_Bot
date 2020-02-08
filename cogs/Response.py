import discord
import json
import aiohttp
from discord.ext import commands


class Responses(commands.Cog):
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

    # Get price of bitcoin from coindesk & post it in usd in chat
    @commands.command()
    async def bitcoinPrice(self, ctx):
        url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
        async with aiohttp.ClientSession() as session:  # Async HTTP request
            raw_response = await session.get(url)
            response = await raw_response.text()
            response = json.loads(response)
            await ctx.send("Bitcoin price is: $" + response['bpi']['USD']['rate'])


# sets up cog to allow it to be used by the bot in main
def setup(bot):
    bot.add_cog(Responses(bot))
