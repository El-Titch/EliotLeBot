import discord
from .RolesView import Roleview
from discord.ext import commands
from discord import app_commands


class Start(discord.Client, commands.Cog):

    def __init__(self, client):
        self.client = client


    async def on_ready(self):
        print(f"Connected as {self.user}")
        channel = self.client.get_channel(int(994322769632309350)) #channel propre au démarrage du bot    
        embed=discord.Embed(title=" 🦌  EliotLeBot est connecté  ⭕ ", description="Le Eliot s'est connecté", color=0x51F56A)
        await channel.purge(limit=10)
        await channel.send(embed=embed)


async def setup(client):
   await client.add_cog(Start(client))
 


