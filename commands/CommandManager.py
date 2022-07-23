import json

from commands.ICmd import ICmd
import commands.list


def get_prefix(message):
    with open('prefixes.json', 'r') as file:
        prefixes = json.load(file)
    return prefixes.get(str(message.guild.id), "*")


class CommandManager:
    def __init__(self, client):
        self.__commands_modules = ICmd.__subclasses__()
        self.__client = client
        print("Loaded commands:")
        self.__commands = []
        for cmd in self.__commands_modules:
            loaded_cmd = cmd()
            self.__commands.append(loaded_cmd)
            print(f" - {loaded_cmd.name()}")
        self.register_message()

    def get_command(self, cmd_name: str) -> ICmd | None:
        for cmd in self.__commands:
            if cmd.name() == cmd_name:
                return cmd
        return None

    def handle_command(self, ctx):
        cmd = self.get_command(ctx.content.replace(get_prefix(ctx), "", 1).split(" ")[0])
        if cmd is None:
            return
        cmd.action(ctx)

    def register_message(self):
        @self.__client.event
        async def on_message(message):
            if message.author == self.__client.user:
                return
            if message.content.startswith(get_prefix(message)):
                self.handle_command(message)
