from EliotLeBot import EliotLeBot
from commands.CommandManager import CommandManager


def main() -> None:
    client = EliotLeBot()
    command_manager = CommandManager(client)
    client.run(open("Token.0", "r", encoding="utf-8").read())


if __name__ == '__main__':
    main()
