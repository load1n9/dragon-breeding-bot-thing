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

"""
Elements:
	1: Fire
	2: Water
	3: Earth
	4: Air
	5: Electric
	6: Wind
	7: Metal
	8: Neon
"""

class Creation(commands.Cog):
    def __init__(self, client):
        self.Client = client
    # Common = 60% chance, Rare = 29% chance, Epic = 10% chance, Legendary = 0.9%, Mythical = 0.1%
    @commands.command()
    async def spawn(self, ctx):
        try:
          getUser(ctx.author.id)
        except:
          createUser({
            "data":{
               "name": str(ctx.author.id),
               "dragons": [] 
             }
          })
        chances = random.randint(1, 1010)

        if chances > 0 and chances < 601:
            CommonEmbed = discord.Embed(title = "Common")
            await ctx.channel.send(embed=CommonEmbed)

        elif chances > 600 and chances < 900:
            RareEmbed = discord.Embed(title="Rare", colour = discord.Colour.red())
            await ctx.channel.send(embed=RareEmbed)

        elif chances > 899 and chances < 1000:
          EpicEmbed = discord.Embed(title="Epic", colour = discord.Colour.purple())
          await ctx.channel.send(embed=EpicEmbed)

        elif chances > 999 and chances < 1009:
            LegendaryEmbed = discord.Embed(title="Legendary", colour = discord.Colour.gold())
            await ctx.channel.send(embed=LegendaryEmbed)

        elif chances > 1008 and chances < 1011:
            MythicalEmbed = discord.Embed(title="Mythical", colour = discord.Colour.blue())
            await ctx.channel.send(embed=MythicalEmbed)
            
    @commands.command()
    async def shop(self, ctx):
        shop = discord.Embed(
            title = "Shop",
            colour = discord.Colour.gold()
        )
        shop.add_field(name="Common elements ($500):", value="""
                                                    Fire Crate 
                                                    Water Crate
                                                    Earth Crate
                                                    Air Crate
                                                        """)
        
        shop.add_field(name="Special elements ($700):", value="""
                                                    Electric Crate 
                                                    Metal Crate
                                                    Neon Crate
                                                        """)
        
        shop.add_field(name="Basic crates:", value="""
                                                    Common Crate ($250)
                                                    Rare Crate ($500)
                                                    Epic Crate ($1000)
                                                    Legendary Crate ($2500)
                                                    Mythical Crate ($10.000)
                                                        """)
        await ctx.channel.send(embed=shop)

def setup(client):
    client.add_cog(Creation(client))