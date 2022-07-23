import discord
import config
from discord.ext import commands
from Utils.Utils import custom_id

VIEW_NAME = "RoleView"

class Roleview(discord.ui.View, commands.Cog):
	def __init__(self, client: commands.Bot):
		self.client = client
		super().__init__(timeout=None)


	@discord.ui.button(label="Accepter", emoji="☑️", custom_id = custom_id(VIEW_NAME, config.FOLLOWER_ROLE_ID))
	async def follower_button(self, button: discord.ui.Button, interaction: discord.Interaction):
		await interaction.response.send_message("Vous avez accepté le réglement, bienvenue")
		if type(bot.role) is not discord.Role:
			bot.role = interaction.guild.get_role(FOLLOWER_ROLE_ID)
		if bot.role not in interaction.user.roles:
			await interaction.user.add_roles(bot.role)
			await interaction.response.send_message(f"Le role {bot.role.mention} vous a été attribué!", ephemeral = True)
		else:
			await interaction.user.remove_roles(bot.role)
			await interaction.response.send_message(f"Le role {bot.role.mention} vous a été retiré!", ephemeral = True)


	@discord.ui.button(label = "Notifications", emoji = "️<:twitch:998375739512598558>", custom_id = custom_id(VIEW_NAME, config.NOTIFS_ROLE_ID))
	async def Notif_button(self, button: discord.ui.Button, interaction: discord.Interaction):
		await interaction.response.send_message("Vous avez accepté de recevoir les Notifications de Stream")



async def setup(client):
	await client.add_cog(Roleview(client))


