import discord
from discord.ext import commands 



class Clear(commands.Cog):

    
    @commands.command(aliases=['clear'])
    @commands.has_permissions(manage_messages=True)
    async def Clear(self, ctx, amount=0, member: discord.Member=None, ):
        
        await ctx.channel.purge(limit=amount+1)
        

def setup(client):
    client.add_cog(Clear(client))
  