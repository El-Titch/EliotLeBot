
import discord
from discord.ui import Button, View
from discord import Embed
from discord.ext import commands
from Twitch import *
import json

with open("config.json") as config_file:
	config = json.load(config_file)


class NetNotifs(commands.Cog):

	def __init__(self, client):
		self.client = client


	@commands.command()
	@commands.has_permissions(administrator = True)
	async def twitch(self, ctx, member: discord.Member = None):
		"""Permet d'envoyer une notification du stream"""
		button = Button(label = 'Twitch', emoji = "<:twitch:998375739512598558>️", url = 'https://twitch.tv/eltitch_')
		if not member:
			member = ctx.author

		view = View(timeout = None)
		view.add_item(button)
		channel = self.client.get_channel(int(1001936220315713586)) # channel Notifs

		users = get_users(config["watchlist"])
		params = {
			"user_id": users.values()
		}

		headers = {
			"Authorization": "Bearer {}".format(config["access_token"]),
			"Client-Id": config["client_id"]
		}
		response = requests.get("https://api.twitch.tv/helix/streams", params = params, headers = headers)

		for entry in response.json()["data"]:
			timestamp = datetime.now()
			embed = Embed(title = f'{entry["title"].upper()}', description = f'*{entry["game_name"]}*', url = 'https://www.twitch.tv/Eltitch_', colour = 0xA41CD3)
			embed.set_author(name = f'{entry["user_name"]}', icon_url = member.avatar )
			embed.set_thumbnail(url = 'https://static-cdn.jtvnw.net/jtv_user_pictures/349f3a75-1b0e-4aea-9685-f3211f336e2b-profile_image-70x70.png')
			embed.set_image(url = 'https://static-cdn.jtvnw.net/previews-ttv/live_user_eltitch_-320x180.jpg')
			embed.set_footer(text = f'{timestamp.strftime(r"%I:%M %p")}  {entry["language"]}')
			await ctx.channel.purge(limit = 1)
			await channel.send(content = "Salut <@&998379417279680537> ! Je suis enstreamn n'hésite pas à passer !",embed = embed, view = view)



async def setup(client):
	await client.add_cog(NetNotifs(client))