import discord 
from discord.ext import commands 



class Errors(commands.Cog):

    def __init__(self, client):
        self.client = client
    

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error, member: discord.Member=None):

        if not member:
            member = ctx.author

        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.channel.send("Veuillez entrer tous les arguments requis")

        if isinstance(error, commands.MissingPermissions):
            if member.dm_channel == None:
                await member.create_dm()
            await member.dm_channel.send(content="Vous n'avez pas les permissions nécessaires pour effectuer cette action")
            await ctx.channel.purge(limit=1)
            
        if isinstance(error, commands.MissingRole):
            if member.dm_channel == None:
                await member.create_dm()
            await member.dm_channel.send(content="Vous n'avez pas le Rôle nécessaire pour effectuer cette action")
            await ctx.channel.purge(limit=1)
            



def setup(client):
    client.add_cog(Errors(client))