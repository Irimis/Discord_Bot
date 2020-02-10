"""This class will be used for any functions that require an internet component such as
grabbing information from a database, or grabbing an image"""

import discord
import json
import aiohttp
from discord.ext import commands


class Online(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

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
    bot.add_cog(Online(bot))