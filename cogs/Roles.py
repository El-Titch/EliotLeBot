from .RolesView import Roleview
from discord.ext import commands

class roles(commands.Cog):
    """Créer des boutons pour attribuer des roles"""

    def __init__ (self, client : commands.Bot):
        self.client = client



    @commands.Cog.listener()
    async def on_ready(self):
        self.client.add_view(Roleview())

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def roles(self, ctx: commands.Context):
        """Creates a new role view"""
        await ctx.send("cliquez",view=Roleview())



async def setup(client: commands.Bot):
    await client.add_cog(roles(client))