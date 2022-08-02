from discord.ext import commands
from Utils.Utils import create_voice_channel, get_category_by_name
import discord



class Voicechan(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_voice_state_update(self, member, before, after):
		if after.channel != None:
			if after.channel.name == "Hub":
				channel = await create_voice_channel(after.channel.guild, f'{member.name}'.lower(), category_name = "Temp")

				if channel != None:
					await member.move_to(channel)

			if before.channel != None:
				if before.channel.category.id == get_category_by_name(before.channel.guild, "Temp").id:
					print("User left temp channel")
					if len(before.channel.members) == 0:
						print("channel empty")
						await before.channel.delete()

async def setup(client):
	await client.add_cog(Voicechan(client))