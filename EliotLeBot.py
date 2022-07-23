import discord



intents = discord.Intents.default()
intents.message_content = True

    async def on_ready(self):
        print(f'Logged as {self.user}')
