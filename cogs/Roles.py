from .RolesView import Roleview
from discord.ext import commands


class roles(commands.Cog):


	def __init__(self,client):
		self.client = client

	@commands.Cog.listener()
	async def on_ready(self, client):
		self.client.add_view(Roleview(client))

	@commands.command()
	@commands.has_permissions(administrator=True)
	async def roles(self, client):
		"""Créer des boutons pour attribuer des roles"""
		await client.send("cliquez", view=Roleview(client))



async def setup(client: commands.Bot):
	await client.add_cog(roles(client))
