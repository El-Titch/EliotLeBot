import discord
from discord.utils import get
from discord.ext import commands

class roles(commands.Cog):


    def __init__ (self, client):
        self.client = client



    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, member: discord.Member):
        channel = self.client.get_channel(998373291091841124)   #Id du channel Règles
        if reaction.message.channel.id != channel :
            return
        if member.reaction.emoji == "☑️":
            role = get(self.guild.roles, id=998378262856216638) #Id du role Follower
            await member.add_roles(member, role)




async def setup(client):
    await client.add_cog(roles(client))