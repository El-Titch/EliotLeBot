from discord.ext import commands, tasks


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
        



async def setup(client):
   await client.add_cog(Status(client))
