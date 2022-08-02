import discord
from discord.ext import commands

from Utils.Utils import msg_contains_word
import json
import os
import re
import string

if os.path.exists(os.getcwd() + "/config.json"):

	with open("./config.json") as f:
		configData = json.load(f)

else:
	configTemplate = {"bannedwords" : []}

	with open(os.getcwd() + "/config.json", "w+") as f:
		json.dump(configTemplate, f)


separators = string.punctuation + string.digits + string.whitespace
excluded = string.ascii_letters

bannedwords = configData["bannedwords"]

formatted_word = f"[{separators}]*".join(list(bannedwords))
regex_true = re.compile(fr"{formatted_word}", re.IGNORECASE)
regex_false = re.compile(fr"([{excluded}] + {bannedwords} ) | ({bannedwords}[{excluded}]+)", re.IGNORECASE)



class Banwords(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command()
	@commands.has_permissions(administrator = True)
	async def addBW(self, ctx, word):
		"""Permet d'ajouter un mot à la liste des banned words"""
		if word.lower() in bannedwords:
			await ctx.send("Ce mot est déjà banni")
		else:
			bannedwords.append(word.lower())

			with open("./config.json", "r+") as f:
				data = json.load(f)
				data["bannedwords"] = bannedwords
				f.seek(0)
				f.write(json.dumps(data))
				f.truncate()

			await ctx.message.delete()
			await ctx.send("Le mot a été ajouté à la liste des mots banni")

	@commands.command()
	@commands.has_permissions(administrator = True)
	async def removeBW(self, ctx, word):
		"""Permet de supprimer un mot de la liste des banned words"""
		if word.lower() in bannedwords:
			bannedwords.remove(word.lower())

			with open("./config.json", "r+") as f:
				data = json.load(f)
				data["bannedwords"] = bannedwords
				f.seek(0)
				f.write(json.dumps(data))
				f.truncate()

			await ctx.message.delete()
			await ctx.send("Le mot a été retiré à la liste des mots banni")
		else:
			await ctx.send("Ce mot n'est pas banni")

	@commands.Cog.listener()
	async def on_message(self, message):
		messageAuthor = message.author

		if bannedwords != None and (isinstance(message.channel, discord.channel.DMChannel) == False):
			for bannedword in bannedwords:
				if msg_contains_word(message.content.lower(), bannedword):
					await message.delete()
					await message.channel.send(f"{messageAuthor.mention}, votre message a été supprimé car il contenait un/plusieurs mots banni")




async def setup(client):
	await client.add_cog(Banwords(client))