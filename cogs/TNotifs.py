import json

from discord.ext import commands, tasks
from discord.ext.tasks import loop

from Twitch import get_notifications

class Notifs (commands.Cog):

	def __init__(self, client):
		self.client = client

	@tasks.loop(seconds = 90)
	async def check_twitch_online_streamers(self):
		channel = self.client.get_channel(1001936220315713586)
		notifications = get_notifications()
		for notification in notifications:
			await channel.send("streamer {} est en ligne: {}".format(notification["user_login"], notification))

	with open("config.json") as config_file:
		config = json.load(config_file)

	if __name__ == "__Notifs__":
		check_twitch_online_streamers.start()


async def setup(client):
	await client.add_cog(Notifs(client))