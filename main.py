import discord
from discord.ext import commands
import os
client = commands.Bot(command_prefix="---", help_command=None)

@client.event
async def on_ready():
    print("ready.")
    await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.listening, name= '---'))
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(os.getenv("TOKEN"))