from discord.ext import commands


class MyHelpCommand(commands.MinimalHelpCommand):
	def get_command_signature(self, command):
		return '{0.clean_prefix}{1.qualified_name}{1.signature}'.format(self, command)

class HelpCog(commands.Cog, name = 'Help'):

	def __init__(self, client):
		self._original_help_command = client.help_command
		client.help_command = MyHelpCommand()
		client.help_command.cog = self

	async def cog_unload(self):
		self.client.help_command = self._original_help_command


async def setup(client: commands.Bot):
	await client.add_cog(HelpCog(client))