import config
import re

def custom_id(view:str, id: int) -> str:
	"""Return the View and the ID"""
	return f"{config.CLIENT_NAME}:{view}:{id}"

async def create_voice_channel(guild, channel_name, category_name = "Games", user_limit = 6):

	category = get_category_by_name(guild, category_name)
	await guild.create_voice_channel(channel_name, category = category, user_limit= user_limit)
	channel = get_channel_by_name(guild, channel_name)
	return channel

async def create_text_channel(guild, channel_name, category = "Games", user_limit = 6):

	category = guild.get_category_by_name(guild, category)
	await guild.create_text_channel(channel_name, category = category)
	channel = guild.get_channel_by_name(guild, channel_name)
	return channel

def get_category_by_name(guild, category_name):
	category = None
	for c in guild.categories:
		if c.name == category_name:
			category = c
			break
	return category


def get_channel_by_name(guild, channel_name):
	channel = None
	for c in guild.channels:
		if c.name == channel_name.lower():
			channel = c
			break
	return channel

def msg_contains_word(msg, word):
	return re.search(fr"\b({word})\b", msg) is not None