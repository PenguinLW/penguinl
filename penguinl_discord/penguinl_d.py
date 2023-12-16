import discord
from discord.et import commands



from dotenv import load_dotenv
import os

load_dotenv()

#p_admin_id = os.getenv("p_admin_id")
p_token = os.getenv("p_token")
#dtoken = os.getenv("dtoken")

client = commands.Bot(command_prefi = '!')

@client.event
async def on_ready():
    print("TH")

@client.command()
async def hello(ct):
await ct.send("HE")

client.run(p_token)
