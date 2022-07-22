import time
import discord
import os ,sys
import json
from discord.ext import commands

def get_prefix(client, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]


client = commands.Bot(intents= discord.Intents.default() ,command_prefix = get_prefix)



@client.event
async def on_guild_join(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = '.'

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent = 4 )



@client.event 
async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent = 4 )



@client.command()
async def changeprefix(ctx, prefix):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent = 4 )
    await ctx.send(f'Le préfixe de commande est désomais " {prefix} "')



def restart_bot():
    os.execv(sys.executable, ['python'] + sys.argv)



@client.command(aliases=['reboot'])
@commands.has_role("Devs")
async def restart(ctx):
    channel = client.get_channel(int(994322769632309350))   
    embed=discord.Embed(title=" 🦌  EliotLeBot Reboot  ♻️ ", description=" Eliot redémare ... Patientez 2s", color=0xEFB422)
    await channel.purge(limit=10)
    await channel.send(embed=embed)
    time.sleep(2)
    restart_bot()
    


@client.command(aliases=['Load', 'laod', 'Laod'])
@commands.has_role("Devs")
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    print('Loaded')



@client.command(aliases=['Unload', 'unlaod', 'Unlaod'])
@commands.has_role("Devs")
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    print('Unloaded')



@client.command(aliases=['Reload', 'relaod', 'Relaod'])
@commands.has_role("Devs")
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    print('Reloaded')
    await ctx.send(f'{extension} has been reloaded')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


with open("Token.0", "r", encoding="utf-8") as f:
    bottoken =f.read()


client.run(bottoken)