import discord 
import yt_dlp
import os
from discord.ext import commands

class Tomp3(commands.Cog):



    def __init__(self, client):
        self.client = client



    @commands.command(pass_context = True)
    @commands.has_role("Createur") # Role de Createur desservi manuellement
    async def tomp3(self, ctx, url:str, member: discord.Member=None):
        """Permet de mettre au format MP3 une vidéo youtube"""
        if not member:
            member = ctx.author

        if ctx.channel.id != 1004478381515092168: # Channel mp3 downloader
            await ctx.channel.purge(limit=1)
            await ctx.send(content="Veuillez effectuer cette commande dans le channel prévu à cet effet. *#mp3-downloader* ")  
            return

        """télécharge de youtube en mp3 <cmd link>"""

        ydl_opts = {
        'format' : 'bestaudio/best',
        'noplaylist' : 'True',
        'preferredcodec': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'webm',
            'preferredquality': '192',
            }],
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

        for filename in os.listdir('./'):
            if filename.endswith('.webm'):
                os.rename(filename, filename[:-4] + '.mp3')

        for filename in os.listdir('./'):
            if filename.endswith('.mp3'):
                await ctx.channel.send(file=discord.File(f'./{filename}'))

        for filename in os.listdir('./'):
            if filename.endswith('.mp3'):
                os.remove(f'./{filename}')
            

async def setup(client):
   await client.add_cog(Tomp3(client))
