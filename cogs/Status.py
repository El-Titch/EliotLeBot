import discord
from itertools import cycle
from discord.ext import commands, tasks

client = commands.Bot(command_prefix = '.')
playing = cycle(['Status 1', 'Status 2'])


class Status(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        self.change_status.start()


    def cog_unload(self):
        self.change_status.cancel()

    
    @tasks.loop( seconds = 10.0 )
    async def change_status(self):
        pass
        



def setup(client):
    client.add_cog(Status(client))
