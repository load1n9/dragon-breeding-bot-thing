import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, client):
        self.Client = client
    
    @commands.command()
    async def help(self, ctx, command=None):
      if command == None:
        embed = discord.Embed(
          title = "Dragon Breed Bot",
          colour = discord.Colour.gold()
        )

        # ----------------------------------
        embed.add_field(name="Spawn", value="Spawn a new dragon.", inline=False)
        embed.add_field(name="Dragons", value="Shows your dragons.", inline=False)
        # ----------------------------------
        
        embed.set_footer(text="The prefix for this bot is:  \"---\"   |   This bot was built by Loading... and Pain")
        await ctx.channel.send(embed=embed)
	
    @commands.command()
    async def test(self, ctx):
        await ctx.send("Working.")
  
def setup(client):
    client.add_cog(Help(client))