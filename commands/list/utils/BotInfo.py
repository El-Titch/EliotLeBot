from abc import ABC

from commands.ICmd import ICmd


class BotInfo(ICmd, ABC):
    def __name__(self):
        self.name = "bot-info"

    def __description__(self):
        self.description = "Show bot information's"

    def __action__(self, ctx):
        print(ctx)
