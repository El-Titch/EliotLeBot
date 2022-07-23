import json

from EliotLeBot import client
from commands.ICmd import ICmd


def get_prefix(message):
    with open('/prefixes.json', 'r') as file:
        prefixes = json.load(file)
    return prefixes[str(message.guild.id)]


class CommandManager:
    def __init__(self):
        self.commands = ICmd.__subclasses__()
        print("Loaded commands:")
        for c in self.commands:
            print(f" - {c.name}")
        super().__init__(timeout=None)

    def get_command(self, cmd: str) -> ICmd | None:
        for c in self.commands:
            if c.name == cmd:
                return c()
        return None

    def handle_command(self, ctx):
        cmd = self.get_command(ctx.content.split(" ")[0].replace(get_prefix(ctx), ""))
        if cmd is None:
            return
        cmd.__action__(ctx)

    @commands.Cog.listener
    async def on_ready(self):
        print("Bot is ready!")

    @commands.Cog.listener
    async def on_message(self, message):
        if message.author == client.user:
            return
        if message.content.startswith(get_prefix(message)):
            self.handle_command(message)
