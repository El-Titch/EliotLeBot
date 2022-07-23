from commands.ICmd import ICmd


class BotInfo(ICmd):
    def name(self):
        return "bot-info"

    def description(self):
        return "Show bot information's"

    def action(self, ctx):
        print(ctx)
        pass
