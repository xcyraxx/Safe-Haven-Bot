import discord
from discord import member
from discord.ext import commands
from discord.ext.commands.cog import Cog
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_components import create_select, create_select_option, create_actionrow
from discord_slash.utils.manage_commands import create_option


__GID__ = [869849123963162635, 846609621429780520]


class Admin(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Admin up!")

    @cog_ext.cog_slash(name="ban", description="Ban a user from this server.", guild_ids=__GID__, 
    options=[
               create_option(
                 name="user",
                 description="Select user to ban.",
                 option_type=6,
                 required=True,
               ),
               create_option(
                    name="reason",
                    description="Reason for ban.",
                    option_type=3,
                    required=False
               )
             ])
    async def ban(self, ctx, user, reason=None):
        banned = discord.Embed(
            title = "User Banned",
            description = f"{user.name}#{user.discriminator} was banned by {ctx.author.mention}"
        )
        banned.add_field(name="Reason", value=f"{reason}")
        banned.set_thumbnail(url=user.avatar_url)
        await user.ban(reason = reason)

    @cog_ext.cog_slash(name="kick", description="Kick a user from this server.", guild_ids=__GID__,
    options=[
               create_option(
                 name="user",
                 description="Select user to ban.",
                 option_type=6,
                 required=True,
               ),
               create_option(
                    name="reason",
                    description="Reason for ban.",
                    option_type=3,
                    required=False
               )
             ])
    async def kick(self, ctx, user, reason=None):
        kicked = discord.Embed(
            title = "User Kicked",
            description = f"{user.name}#{user.discriminator} was kicked by {ctx.author.mention}"
        )
        kicked.add_field(name="Reason", value=f"{reason}")
        kicked.set_thumbnail(url=user.avatar_url)
        await user.kick(reason = reason)

    @cog_ext.cog_slash(name="mute", description="Mute a user", guild_ids=__GID__, 
    options=[
               create_option(
                 name="member",
                 description="Select user to ban.",
                 option_type=6,
                 required=True,
               ),
               create_option(
                    name="reason",
                    description="Reason for ban.",
                    option_type=3,
                    required=False
               )
             ])
    async def mute(self, ctx, member, reason=None):
        #await ctx.defer()
        if ctx.author.guild_permissions.manage_roles:
            mod_channel = self.client.get_channel(869849124537778214)
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
                                description=f"{member.mention} was muted\n\nBy: {ctx.author.mention}",
                                color=discord.Color.from_rgb(73, 131, 179))
            embed.add_field(name="reason:", value=reason, inline=False)
            embed.set_thumbnail(url=member.avatar_url)
            await mod_channel.send(embed=embed)
            await member.add_roles(mutedRole, reason=reason)
            await ctx.send(embed=embed)
        else:
            await ctx.send("Come back with admin permissions ^-^")


    @cog_ext.cog_slash(name="help", description="Shows the basic commands", guild_ids=__GID__)
    async def _help(self, ctx: SlashContext):
        select = create_select(
            options=[# the options in your dropdown
                create_select_option("Moderation", value="modz", emoji="🛡️"),
                create_select_option("Music", value="m00sik", emoji="🎶"),
                create_select_option("Other", value="other", emoji="🗿"),
            ],
            placeholder="Select Category",  # the placeholder text to show when no options have been chosen
            min_values=1,  # the minimum number of options a user must select
            max_values=1,  # the maximum number of options a user can select
        )

        action_row = create_actionrow(select)
        bot_help = discord.Embed(
            title="Safe Haven Help",
            description="Select Category for commands.",
            color=discord.Color.from_rgb(73, 131, 179))
        await ctx.send(embed = bot_help, components = [action_row])

def setup(bot):
    "Setup command for the bot"

    bot.add_cog(Admin(bot))