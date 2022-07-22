from logging import shutdown
import discord
from discord.ext import commands


client = commands.Bot(command_prefix = '.')



class Start(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_ready(self):
        print("Connected")
        channel = self.client.get_channel(int(994322769632309350)) #channel propre au démarrage du bot    
        embed=discord.Embed(title=" 🦌  EliotLeBot est connecté  ⭕ ", description="Le Eliot s'est connecté", color=0x51F56A)
        await channel.purge(limit=10)
        await channel.send(embed=embed)



    @commands.command()
    async def logout(self, ctx):
        channel = self.client.get_channel(int(994322769632309350))
        embed=discord.Embed(title=" 🦌  EliotLebot est déconnecté ❌ ", description="Le Eliot s'est déconnecté", color=0xff3737)
        await ctx.channel.purge(limit=10)
        await ctx.channel.send(embed=embed)
        await ctx.shutdown




def setup(client):
    client.add_cog(Start(client))
 


