import discord
import config
from discord.ui import Button
from discord.ui import View
from discord.ext import commands
from Utils.Utils import custom_id


VIEW_NAME = "Roleview"


class embed(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def rules(self, ctx):
        button_notif = Button(label="Notifications", emoji="<:twitch:998375739512598558>️", custom_id = custom_id(VIEW_NAME, config.NOTIFS_ROLE_ID))
        button_Follower = Button(label = "Accepter", emoji = "☑️", custom_id = custom_id(VIEW_NAME, config.FOLLOWER_ROLE_ID))

        async def Fbutton_callback(interaction):
            Follower = interaction.guild.get_role(998378262856216638)  # Role Follower
            if Follower not in interaction.user.roles:
                await interaction.user.add_roles(Follower)
                await interaction.response.send_message(content = "Vous avez accepté le règlement, bienvenue !", ephemeral = True)
            else:
                await interaction.response.send_message(content = "Vous avez déjà accepté le règlement !", ephemeral = True)

        async def Nbutton_callback(interaction):
            Notifs = interaction.guild.get_role(998379417279680537) # Role Notifs
            if Notifs not in interaction.user.roles:
                await interaction.user.add_roles(Notifs)
                await interaction.response.send_message("Le rôle Notifs vous a été attribué ", ephemeral = True)
            else:
                await interaction.user.remove_roles(Notifs)
                await interaction.response.send_message("Le rôle Notifs vous a été retiré", ephemeral = True)

        button_Follower.callback = Fbutton_callback
        button_notif.callback = Nbutton_callback


        view = View(timeout = None)
        view.add_item(button_Follower)
        view.add_item(button_notif)
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
> • Si vous souhaitez être mentionné via annonces  lors des lancement de lives, veuillez cocher :twitch: """, view = view)


intents = discord.Intents.default()
intents.members = True


async def setup(client):
   await client.add_cog(embed(client))
