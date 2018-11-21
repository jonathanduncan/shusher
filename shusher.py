import asyncio
from discord.ext import commands

class Shush:
    def __init__(self):
        self.timer = 0
        self.state = ''

    @commands.command(pass_context=True, no_pm=True)
    async def summon(self, ctx):

bot = commands.Bot(command_prefix=commands.when_mentioned_or('!'), description='A bot tht shushes for the sake of '
                                                                               'productivity.')
bot.add_cog(Shush(bot))
bot.run('NDI0NjQyNjYzMjAzOTk1NjQ4.DY73zQ.fxN6wrlpGXmmL2_QzSeKZITmNKs')

@bot.event
async def on_ready():
    print(f'Logged in as: {bot.user}\nID: {bot.user.id}')
