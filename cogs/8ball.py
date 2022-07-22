import discord
import random
from discord.ext import commands

client = commands.Bot

class _8ball(commands.Cog): 

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['8ball'])

    async def _8ball(self, ctx, *, question):
        responses = ["C'est certain.",
                 "C'est décidément ainsi",
                 'Sans aucun doute.',
                 'Définitivement oui.',
                 'Vous pouvez vous y fier.',
                 'Comme je le perçois, oui.',
                 'Probablement.',
                 'Les perspectives sont favorable.',
                 'Oui.',
                 'Les signes pointes vers oui.',
                 'Redemandez plus tard.',
                 'Mieux vaut ne pas vous le dire maintenant.',
                 'Je ne peux pas le prédire pour le moment.',
                 "Ne comptais pas dessus.",
                 'Ma réponse est non.',
                 'Mes sources disent Non.',
                 'Les perspectives ne sont pas favorable.',
                 'Il y a beaucoup de doute.']
        channel = self.client.get_channel(int(992790270875799662)) # channel spécifique au 8ball
        await channel.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


def setup(client):
    client.add_cog(_8ball(client))