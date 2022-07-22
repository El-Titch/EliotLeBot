import discord
from discord.ext import commands

class Ping(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['ping'])
    async def Ping(self, ctx):
        await ctx.send(f'Delay of {round(self.client.latency * 1000)}ms')



async def setup(client):
   await client.add_cog(Ping(client))