import discord 
from discord.ext import commands

class embed(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command()
    @commands.has_role(994248476055588865) # Role devs
    async def rules(self, ctx):
        await ctx.channel.purge(limit=2)
        await ctx.send("""**Réglement** 

*Bonjour/Bonsoir à vous et bienvenue sur ce serveur. * 

*Avant d'aller plus loin, il va être nécessaire de lire et comprendre les règles du serveur.*   

*Pas de panique rien de bien compliqué *:wink: 


:tophat:** Les Bonnes manières**
> • Le respect mutuel n'est pas une option.
> • Les discours Haineux, Homophobes, Politiques, Raciste et Religieux seront puni d'un bannissement permanent.
> • La diffusion de contenu NSFW, Pornographique, Violent (Hors jeux-vidéo) de quelconque manière que ce soit est interdite et sera puni d'un bannissement permanent
> • Les Pseudonymes et Photos de profils indécentes sont interdites

:writing_hand: ** A L'écrit**
> • Mentionner un membre du staff de manière abusive est interdite
> • Le Spam n'est ni utle, ni agréable. Il est donc proscrit.

:speaking_head: ** A L'oral**
> • L'utilisation de modificateur de voix et/ou de soundboard est interdite.
> • Le changement rapide et répéter de channel vocal est interdit
> • La diffusion de contenue innaproprié via la fonction Stream est interdite.

:shield:  Sanctions  
> • 1° Avertissement : 30 min de Time Out.
> • 2° Avertissement : 1 jour de Bannissement.
> • 3° Avertissement : Bannissement permanent.
> • Si la sanction est spécifié dans la règle, s'y référer. 

:large_orange_diamond: Les Rôles
> • Pour votre confort, il vous est conseillé de lier vos compte twitch et dicord afin de synchroniser votre Sub.
> • Si vous avez lu et compris le réglement du serveur, veuillez cocher la réaction :ballot_box_with_check:
> • Si vous souhaitez être mentionné via annonces  lors des lancement de lives, veuillez cocher :twitch: """)
        


async def setup(client):
   await client.add_cog(embed(client))