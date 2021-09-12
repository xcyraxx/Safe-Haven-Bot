import discord
from discord.ext import commands
from discord.ext.commands import Cog
import asyncio

class Reminder(commands.Cog):
    def __init__(self, client):
        self.client=client

    @Cog.listener()
    async def on_ready(self):
        print('Reminder up!')

    @commands.command()
    async def reminder(self, ctx, time: int, *, reason=None):
        await ctx.send(f"I'll ping you in {time} hour(s)")
        hour = time*3600
        print(hour)
        await asyncio.sleep(int(hour))
        await ctx.send(f"{ctx.author.mention}. {reason}")


def setup(bot):
    bot.add_cog(Reminder(bot))
