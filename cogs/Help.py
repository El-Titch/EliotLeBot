import discord
from discord import Embed
from discord.ext import commands

client = commands.Bot (command_prefix = "*", intents = discord.Intents.default())

class MyHelp(commands.MinimalHelpCommand):
	async def send_pages(self):
		destination = self.get_destination()
		for page in self.paginator.pages:
			embed = Embed(description = page)
			await destination.send(embed = embed)




class MyCog (commands.Cog):
	def __init__(self, client):
		self.client = client
		self._original_help_command = client.help_command
		client.help_command = MyHelp()
		client.help_command.cog = self


	def cog_unload(self):
		self.client.help_command = self._original_help_command

async def setup(client):
	await client.add_cog(MyCog(client))