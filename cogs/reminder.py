import discord
from discord.ext import commands
from discord.ext.commands import Cog
import asyncio
import datetime, time

class Reminder(commands.Cog):
    def __init__(self, client):
        self.client=client

    @Cog.listener()
    async def on_ready(self):
        print('Reminder up!')
        global startTime 
        startTime = time.time()

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

    @commands.command()
    async def serverinfo(self, ctx):
        infobed = discord.Embed(
            title="Server Info",
            color=discord.Color.orange()
        )
        infobed.add_field(name="Server ID", value=ctx.guild.id, inline=True)
        infobed.add_field(name="Created On", value=ctx.guild.created_at.strftime("%a, %b %d, %Y %I:%M %p\n"))
        infobed.add_field(name="Owner", value=f"{ctx.guild.owner.name}#{ctx.author.discriminator}", inline=False)
        infobed.add_field(name="Owner ID", value=ctx.guild.owner.id)
        infobed.add_field(name="Total Roles", value=len(ctx.guild.roles))
        infobed.add_field(name="Top Role", value=ctx.guild.roles[len(ctx.guild.roles)-1])
        infobed.add_field(name="Total Members", value=len([m for m in ctx.guild.members if not m.bot]))
        infobed.add_field(name="Total Bots", value = len([m for m in ctx.guild.members if m.bot]))
        infobed.set_thumbnail(url=ctx.guild.icon_url)
        infobed.set_author(name=ctx.guild.owner.name, icon_url=ctx.guild.owner.avatar_url)
        await ctx.send(embed=infobed)


def setup(bot):
    bot.add_cog(Reminder(bot))
