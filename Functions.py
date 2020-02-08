from discord.ext import commands
bot = commands.Bot(command_prefix='$')


# Get users botToken to login to discord servers
def login():
    botToken = input("Enter your bot token: ")
    return botToken
