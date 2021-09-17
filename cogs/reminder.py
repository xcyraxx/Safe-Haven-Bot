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

    @commands.command(name="botinfo", aliases=("bi", ))
    async def command_botinfo(self, ctx):
        "Returns information about the bot"
        user = ctx.guild.get_member(879624970492325938)
        info = discord.Embed(
            title="Bot Info",
            color=discord.Color.from_rgb(252, 165, 3)
        )
        info.set_author(name=f"{user.display_name}#{user.discriminator}", icon_url=user.avatar_url)
        info.add_field(name="ID", value=self.client.user.id, inline=True)
        info.add_field(name="Created on",
                    value=user.created_at.strftime("%a, %b %d, %Y %I:%M %p"))
        #info.add_field(name="Joined on", value=member.joined_at.strftime("%a, %b %d, %Y %I:%M %p"))
        uptime = str(datetime.timedelta(seconds=int(round(time.time()-startTime))))
        info.add_field(name="Library used", value="Enhanced Discord.py v1.7.3.7.post1", inline=False)
        info.add_field(name="Python Version", value="Python 3.9.6", inline=True)
        info.add_field(name="Code Lines written", value="1992")
        info.add_field(name="Uptime", value=uptime, inline=False)
        info.add_field(name="Top Role in this Server" ,value=user.top_role)
        info.add_field(name="Version", value="1.8.0", inline=False)
        info.set_footer(text="Bot created by Adil#5514")
        info.set_thumbnail(url=user.avatar_url)
        await ctx.send(embed=info)



def setup(bot):
    bot.add_cog(Reminder(bot))
