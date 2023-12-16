##https://discord.com/developers/docs/intro
##https://discordpy.readthedocs.io/en/stable/api.html#discord.Intents
##https://discordpy.readthedocs.io/en/latest/intents.html
import discord
from discord.ext import commands
from discord.ext import tasks
from discord.ext.commands import has_permissions, MissingPermissions
from discord.utils import get



from dotenv import load_dotenv
import os

load_dotenv()

#p_admin_id = os.getenv("p_admin_id")
p_token = os.getenv("p_token")
#dtoken = os.getenv("dtoken")

intents = discord.Intents.all()
intents.members = True
intents.typing = True
intents.presences = False
intent.message_content = True

client = commands.Bot(command_prefix = '!', intents = intents)

@client.event
async def on_ready():
    print("TH")

@client.command()
async def hello(ctx):
    await ctx.send("HE")

client.run(p_token)
