import discord
from discord.ext import commands
from Utils.Utils import get_channel_by_name


class Start(commands.Cog):

    def __init__(self, client):
        self.client = client


    async def on_ready(self, ctx):
        print(f"Connected")
        channel = self.client.get_channel_by_name(ctx.guild, "annonces") #channel propre au démarrage du bot
        embed=discord.Embed(title=" 🦌  EliotLeBot est connecté  ⭕ ", description="Le Eliot s'est connecté", color=0x51F56A)
        await channel.purge(limit=10)
        await channel.send(embed=embed)


async def setup(client):
   await client.add_cog(Start(client))
 


