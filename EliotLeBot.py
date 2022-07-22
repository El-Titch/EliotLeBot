import time
import discord
import os
import sys
import json
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True


def get_prefix(message):
    with open('prefixes.json', 'r') as file:
        prefixes = json.load(file)


    return prefixes[str(message.guild.id)]


client = commands.Bot(command_prefix = get_prefix, intents = intents)

@client.event
async def on_guild_join(guild):
    with open('prefixes.json', 'r') as file:
        prefixes = json.load(file)

    prefixes[str(guild.id)] = '.'

    with open('prefixes.json', 'w') as file:
        json.dump(prefixes, file, indent = 4)


@client.event 
async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as file:
        prefixes = json.load(file)

    prefixes.pop(str(guild.id))

    with open('prefixes.json', 'w') as file:
        json.dump(prefixes, file, indent = 4)


@client.command()
async def changeprefix(ctx, prefix):
    with open('prefixes.json', 'r') as file:
        prefixes = json.load(file)

    prefixes[str(ctx.guild.id)] = prefix

    with open('prefixes.json', 'w') as file:
        json.dump(prefixes, file, indent = 4)
    await ctx.send(f'Le préfixe de commande est désomais " {prefix} "')


def restart_bot():
    os.execv(sys.executable, ['python'] + sys.argv)


@client.command(aliases=['reboot'])
@commands.has_role("Devs")
async def restart(ctx):
    channel = client.get_channel(int(994322769632309350))   
    embed = discord.Embed(title=" 🦌  EliotLeBot Reboot  ♻️ ", description=" Eliot redémare ... Patientez 2s", color=0xEFB422)
    await channel.purge(limit=10)
    await channel.send(embed=embed)
    time.sleep(2)
    restart_bot()


@client.command(aliases=['Load'])
@commands.has_role("Devs")
async def load(ctx, extension):
    await client.load_extension(f'cogs.{extension}')
    print('Loaded')
    await ctx.send(f'{extension} has been Loaded ')


@client.command(aliases=['Unload'])
@commands.has_role("Devs")
async def unload(ctx, extension):
    await client.unload_extension(f'cogs.{extension}')
    print('Unloaded')
    await ctx.send(f'{extension} has been Unloaded')


@client.command(aliases=['Reload'])
@commands.has_role("Devs")
async def reload(ctx, extension):
    await client.unload_extension(f'cogs.{extension}')
    await client.load_extension(f'cogs.{extension}')
    print('Reloaded')
    await ctx.send(f'{extension} has been reloaded')

@client.event
async def on_ready():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await client.load_extension(f'cogs.{filename[:-3]}')

with open("Token.0", "r", encoding="utf-8") as file:
    bottoken = file.read()


client.run(bottoken)
