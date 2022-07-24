import discord
from discord.ext import commands 

client = commands.Bot

class Clear(commands.Cog):

    def __init__(self):
        self.client = client

    @commands.command(aliases=['clear'])
    @commands.has_permissions(manage_messages=True)
    async def Clear(self, *, ctx, amount=0, member: discord.Member=None ):
        """Commande pour supprimer les messages"""
        await ctx.channel.purge(limit=amount+1)


async def setup(client):
    await client.add_cog(Clear(client))
  