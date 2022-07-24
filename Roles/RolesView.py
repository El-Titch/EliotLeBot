import discord
import config
from Utils.Utils import custom_id
from discord.ui import View
from discord.ui import Button


VIEW_NAME = "RoleView"

class Roleview(View):
	def __init__(self):
		super().__init__(timeout=None)


	@discord.ui.button(label = "Notifications", emoji = "️<:twitch:998375739512598558>", custom_id = custom_id(VIEW_NAME, config.NOTIFS_ROLE_ID))
	async def notifs_button(self, interaction):
		Notifs = interaction.guild.get_role(config.NOTIFS_ROLE_ID)
		if Notifs not in interaction.user.role:
			await interaction.user.add_roles(Notifs)
			await interaction.response.send_message("Le Role Notifs vous a été attribué !", ephemeral = True)
		else:
			await interaction.user.remove_roles(Notifs)
			await interaction.response.send_message("Le Role Notifs vous a été retiré !", ephemeral = True)


	@discord.ui.button(label="Accepter", emoji="☑️", custom_id = custom_id(VIEW_NAME, config.FOLLOWER_ROLE_ID))
	async def Follower_button(self, button, interaction: discord.Interaction):
		Follower = interaction.guild.get_role(config.FOLLOWER_ROLE_ID)
		if Follower not in interaction.user.role:
			await interaction.user.add_roles(Follower)
			await interaction.response.send_message("Vous avez accepté le règlement, bienvenue !", view = None, ephemeral = True)




