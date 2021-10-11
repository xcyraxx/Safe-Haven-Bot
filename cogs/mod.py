import discord
import discord.ext
from discord.ext import commands
from discord.ext.commands import Cog
from discord_slash import SlashCommand, cog_ext, SlashContext

__GID__ = [869849123963162635, 846609621429780520]

class Mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Mod up!")

    @cog_ext.cog_slash(name="kick", description="Kick a user", guild_ids=__GID__)
    async def kick(self, ctx: SlashContext, user: discord.Member, *, reason="No reason provided"):
        if ctx.author.guild_permissions.administrator:
            mod_channel = self.bot.get_channel(869849124537778214)
            await user.kick(reason=reason)
            ban = discord.Embed(
                title=f"Kicked {user.name}!",
                description=f"Reason: {reason}\nBy: {ctx.author.mention}",
                color=discord.Color.from_rgb(73, 131, 179))
            await mod_channel.send(embed=ban)
            await ctx.send("User Kicked.")
            await user.send(embed=ban)
            await ctx.message.delete()
        else:
            await ctx.send("Come back with admin permissions ^-^")

    @cog_ext.cog_slash(name="ban", description="Ban a user", guild_ids=__GID__)
    async def ban(self, ctx: SlashContext, user: discord.Member, *, reason="No reason provided"):
        if ctx.author.guild_permissions.administrator:
            mod_channel = self.bot.get_channel(869849124537778214)
            await user.ban(reason=reason)
            ban = discord.Embed(
                title=f"Banned {user.name}!",
                description=f"Reason: {reason}\nBy: {ctx.author.mention}",
                color=discord.Color.from_rgb(73, 131, 179))
            await mod_channel.send(embed=ban)
            await ctx.send(f"{user.name} Kicked.")
            await user.send(embed=ban)
            await ctx.message.delete()
        else:
            await ctx.send("Come back with admin permissions ^-^")

    @cog_ext.cog_slash(name="mute", description="Mute a user", guild_ids=__GID__)
    async def mute(self, ctx: SlashContext, member: discord.Member, *, reason=None):
        await ctx.defer()
        if ctx.author.guild_permissions.manage_roles:
            mod_channel = self.bot.get_channel(869849124537778214)
            guild = ctx.guild
            mutedRole = discord.utils.get(guild.roles, name="Muted")

            if not mutedRole:
                mutedRole = await guild.create_role(name="Muted")

                for channel in guild.channels:
                    await channel.set_permissions(mutedRole,
                                                speak=False,
                                                send_messages=False,
                                                read_message_history=True,
                                                read_messages=True)
            embed = discord.Embed(title="User Muted",
                                description=f"{member.mention} was muted\nBy: {ctx.author.mention}",
                                color=discord.Color.from_rgb(73, 131, 179))
            embed.add_field(name="reason:", value=reason, inline=False)
            await mod_channel.send(embed=embed)
            await member.add_roles(mutedRole, reason=reason)
            await ctx.send(embed=embed)
        else:
            await ctx.send("Come back with admin permissions ^-^")

def setup(bot):
    bot.add_cog(Mod(bot))