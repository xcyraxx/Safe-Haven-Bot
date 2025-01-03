import discord
from discord import client
import discord.ext
import re
from discord.ext import commands
import asyncio
from discord_slash.utils.manage_commands import create_option
import random
from discord.ext.commands import Cog
from discord_slash import SlashCommand, cog_ext, SlashContext

__GID__ = [869849123963162635, 846609621429780520]


class Giveaway(commands.Cog):
    def __init__(self, client):
        self.client = client

    @Cog.listener()
    async def on_ready(self):
        print('Giveaway up!')

    @cog_ext.cog_slash(name="giveaway", description="Start a giveaway", guild_ids=__GID__, 
    options=[
               create_option(
                 name="channel",
                 description="Channel to start the giveaway in.",
                 option_type=7,
                 required=True,
               )
             ])
    async def command_giveaway(self, ctx, channel):
        if channel:
                await ctx.send("Enter Giveaway item Name.")
                item = await self.client.wait_for('message', check=lambda m: m.author == ctx.author, timeout=60)
                await ctx.send("Noice, now how long do you want the Giveaway to last? eg: 2d, 1h, 4m (use d, h and m for days, hours and minutes")
                time = await self.client.wait_for('message', check=lambda m: m.author == ctx.author, timeout=60)
                await ctx.send("Cool, How many winners?")
                winners = await self.client.wait_for('message', check=lambda m: m.author == ctx.author, timeout=60)
                
                a = re.split(r'(\d+)', time.content)
                nano = ""
                if a[2] == 'd':
                    time = int(a[1])*86400
                    nano = "Day(s)"
                elif a[2] == 'm':
                    time = int(a[1])*60
                    nano = "Minute(s)"
                elif a[2] == 'h':
                    time = int(a[1])*3600
                    nano = "Hour(s)"
                init = discord.Embed(title=item.content,
                                    description=f"React with 🎉 to enter!\nEnds: in {a[1]} {nano}\nHosted by: {ctx.author.mention}",
                                    color=discord.Color.from_rgb(73, 131, 179)
                )
                init.set_footer(text=f"Total Winners: {winners.content}")
                await channel.send("🎉**GIVEAWAY**🎉")
                initembed = await channel.send(embed=init)
                init_id = initembed.id
                await initembed.add_reaction("🎉")
                await ctx.send(f"🎉 Ay! The Giveaway has started in {channel}!")

                new_msg = await channel.fetch_message(init_id)

                await asyncio.sleep(time)

                users = await new_msg.reactions[0].users().flatten()
                winner = random.choice(users)
                await channel.send(f"Congrats {winner.mention}, you won the {item.content}")
                final = discord.Embed(title=item.content,
                                    description=f"**Winner:** {winner}\n**Hosted By:** {ctx.author.mention}",
                                    color=discord.Color.from_rgb(73, 131, 179)
                )
                final.set_footer(text="Thank you for participating!")
                giv = await channel.fetch_message(init_id)
                await giv.edit(embed=final)

    

        else:
            await ctx.send("Specify a channel to run the giveaway in. Usage: `=giveaway #channel`")


def setup(bot):
    bot.add_cog(Giveaway(bot))
