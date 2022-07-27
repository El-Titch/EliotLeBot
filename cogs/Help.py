from typing import Optional

import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot (command_prefix = "*", intents = intents)

class MyHelp(commands.HelpCommand):
	def get_command_signature(self, command):
		return "%s%s %s" % (self.context.clean_prefix, command.qualified_name, command.signature)

	async def help_embed(self, title: str, description: Optional[str] = None, mapping: Optional[dict] = None, command_set: Optional[list[commands.Command]] = None ):
		embed = discord.Embed(title = title)
		if description:
			embed.description = description
		if command_set:
			filtered = await self.filter_commands(command_set, sort = True)
			for command in filtered:
				embed.add_field(name = f'`{self.get_command_signature(command)}`', value = command.help, inline = False)
				alias = command.aliases
				if alias:
					embed.add_field(name = '***Alias*** : ', value = ", ".join(alias), inline = True)
		elif mapping:
			for cog, command in mapping.items():
				filtered = await self.filter_commands(command, sort = True)
				if not filtered:
					continue
				name = f'***{cog.qualified_name}***' if cog else "***Developer***"
				cmd_list = "\u2002".join(
					f"`{self.context.clean_prefix}{cmd.name}`" for cmd in filtered
				)
				value = (
					f"{cog.description}\n{cmd_list}"
					if cog and cog.description
			        else cmd_list
				)
				embed.add_field(name = name, value = value)
		return embed

	async def send_bot_help(self, mapping: dict):
		embed = await self.help_embed(
			title = 'Les Commandes',
			description = self.context.bot.description,
			mapping=mapping
		)
		await self.get_destination().send(embed = embed)

	async def send_command_help(self, command: commands.Command):
		embed = await self.help_embed(
			title = command.qualified_name,
			description = command.help,
			command_set = command.commands if isinstance(command, commands.Group) else None

		)

		await self.get_destination().send(embed = embed)

	async def send_cog_help(self, cog: commands.Cog):
		embed = await self.help_embed(
			title = cog.qualified_name,
			description = cog.description,
			command_set = cog.get_commands()
		)
		await self.get_destination().send(embed = embed)

	send_group_help = send_command_help


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