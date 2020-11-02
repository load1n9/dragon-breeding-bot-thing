import discord
import random
from discord.ext import commands
from cogs.utils.db import getUser, createUser
"""Dragons = [
            CommonDragons[]
            RareDragons[]
            EpicDragons[],
            LegendaryDragons[]
            MythicalDragons[]
          ]"""


class Creation(commands.Cog):
    def __init__(self, client):
        self.Client = client
    # Common = 60% chance, Rare = 29% chance, Epic = 10% chance, Legendary = 0.9%, Mythical = 0.1%
    @commands.command()
    async def spawn(self, ctx):
        try:
          print(getUser(ctx.author.id))
        except:
          createUser({
            "data":{
               "name": str(ctx.author.id),
               "dragons": [] 
             }
          })
        chances = random.randint(1, 1010)

        if chances > 0 and chances < 601:
            CommonEmbed = discord.Embed(title = "Common", colour = discord.Colour.gold())
            await ctx.channel.send(embed=CommonEmbed)

        elif chances > 600 and chances < 900:
            RareEmbed = discord.Embed(title="Rare", colour = discord.Colour.red())
            await ctx.channel.send(embed=RareEmbed)

        elif chances > 899 and chances < 1000:
			EpicEmbed = discord.Embed(title="Epic", colour = discord.Colour.purple())
			await ctx.channel.send(embed=EpicEmbed)

        elif chances > 999 and chances < 1009:
            LegendaryEmbed = discord.Embed(title="Legenday", colour = discord.Colour.red())
            await ctx.channel.send(embed=LegendaryEmbed)

        elif chances > 1008 and chances < 1011:
            await ctx.channel.send("Mythical")

def setup(client):
    client.add_cog(Creation(client))