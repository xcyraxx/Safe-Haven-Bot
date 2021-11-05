from os import name
import discord
from discord import channel
from discord.ext import commands
from discord.ext.commands import Cog
from discord import Embed, Forbidden
import time
from datetime import datetime
import discord
from discord.utils import get

class Log(Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @Cog.listener()
    async def on_ready(self):
        print('logs up!')
        self.channel=self.bot.get_channel(869849124537778214)
        self.plus = self.bot.get_emoji(906285613295235092)
        self.minus = self.bot.get_emoji(906285811417354340)
        
    
    @Cog.listener()
    async def on_user_update(self, before, after):
        if before.name != after.name:
            embed = Embed(title="Member Update",
             description=f"{after.name}#{after.discriminator}'s Username was changed",
              color=discord.Color.from_rgb(73, 131, 179),
               timestamp = datetime.utcnow())

            fields = [("Before", before.name, False),
                      ("After", after.name, False)]

            for name, value, inline in fields:
                embed.add_field(name=name, value=value, inline=inline)
            await self.channel.send(embed=embed)

        if before.avatar_url != after.avatar_url:
            embed = Embed(title="Member Update",
             description=f"{after.name}#{after.discriminator}'s Avatar was changed",
              color=discord.Color.from_rgb(73, 131, 179),
               timestamp = datetime.utcnow())

            fields = [("Before", before.avatar_url, False),
                      ("After", after.avatar_url, False)]

            for name, value, inline in fields:
                embed.add_field(name=name, value=value, inline=inline)
            await self.channel.send(embed=embed)

    @Cog.listener()
    async def on_member_update(self, before, after):
        if before.display_name != after.display_name:
            embed = Embed(
             description=f"{after.mention} updated their nickname.",
              color=discord.Color.from_rgb(73, 131, 179),
               timestamp = datetime.utcnow())
            embed.add_field(name="New Name", value=after.display_name, inline=False)
            embed.add_field(name="Old Name", value=before.display_name, inline=False)
            embed.add_field(name="ID", value=f"```ini\nUser = {after.id}\n```", inline=False)
            embed.set_author(name=f"{after.name}#{after.discriminator}", icon_url=after.avatar_url)
            await self.channel.send(embed=embed)

        elif before.roles != after.roles:
            embed = Embed(
                description=f"{after.mention}\'s roles were updated ",
                color=discord.Color.from_rgb(73, 131, 179),
                timestamp = datetime.utcnow()
                )
            changed_role_set = set(before.roles) ^ set(after.roles)
            if len(changed_role_set) > 0:
                changed_role = next(iter(changed_role_set))
                #and then answer
            if changed_role in after.roles:
                embed.add_field(name="Role Added", value=f"{self.plus} {changed_role.mention}", inline=False)
            else:
                embed.add_field(name="Role Removed", value=f"{self.minus} {changed_role.mention}", inline=False)
            
            embed.add_field(name="ID", value=f"```ini\nUser = {after.id}\nRole = {changed_role.id}\n```", inline=False)
            embed.set_author(name=f"{after.name}#{after.discriminator}", icon_url=after.avatar_url)
            await self.channel.send(embed=embed)

    @Cog.listener()
    async def on_message_edit(self, before, after):
        if not after.author.bot:
            if before.content != after.content:
                embed = Embed(
            description=f"**{after.author.name}#{after.author.discriminator}** updated their message in: {after.channel}",
            color=discord.Color.from_rgb(73, 131, 179),
            timestamp = datetime.utcnow()
            )
                embed.add_field(name="Channel", value=f"{after.channel.mention}({after.channel})\n[Go to Message]({after.jump_url})", inline=False)
                embed.add_field(name="Now", value=f"{after.content}", inline=False)
                embed.add_field(name="Previous", value=f"{before.content}", inline=False)
                embed.add_field(name="ID", value=f"```ini\nUser = {after.author.id}\nMessage = {after.id}\n```", inline=False)
                embed.set_author(name=after.author.name, icon_url=after.author.avatar_url)  
                await self.channel.send(embed=embed)

            

    @Cog.listener()
    async def on_message_delete(self, message):
        if not message.author.bot:
            embed = Embed(
             description=f"Message deleted in {message.channel.mention}",
             color=discord.Color.from_rgb(73, 131, 179),
               timestamp = datetime.utcnow())
            embed.add_field(name="Content", value=f"{message.content}", inline=False)
            embed.add_field(name="Date", value=f"<t:{int(time.time())}:F>", inline=False)
            embed.add_field(name="ID", value=f"```ini\nUser = {message.author.id}\nMessage = {message.id}\n```", inline=False)
            embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
            await self.channel.send(embed=embed)   

        
    @Cog.listener()
    async def on_channel_delete(self, channel):
        embed = Embed(
             description=f"Channel deleted: {channel.mention}",
             color=discord.Color.from_rgb(73, 131, 179),
               timestamp = datetime.utcnow())
        embed.add_field(name="ID", value=f"```ini\nChannel = {channel.id}\n```", inline=False)
        embed.set_author(name=channel.name, icon_url=channel.guild.icon_url)
        await self.channel.send(embed=embed)


    @Cog.listener()
    async def on_guild_channel_create(self, channel):
        embed = Embed(
             description=f"Channel created: {channel.mention}",
             color=discord.Color.from_rgb(73, 131, 179),
               timestamp = datetime.utcnow())
        embed.add_field(name="ID", value=f"```ini\nChannel = {channel.id}\n```", inline=False)
        embed.set_author(name=channel.name, icon_url=channel.guild.icon_url)
        await self.channel.send(embed=embed)

    @Cog.listener()
    async def on_guild_channel_update(self, before, after):
        if before.name != after.name:
            embed = Embed(
             description=f"Text Channel was updated ({after.name})",
             color=discord.Color.from_rgb(73, 131, 179),
               timestamp = datetime.utcnow())
            embed.add_field(name="Created on", value=f"<t:{int(after.created_at.timestamp())}:F>", inline=False)
            embed.add_field(name="Name", value=f"Previous: {before.name}\n Now: {after.name}", inline=False)
            embed.add_field(name="ID", value=f"```ini\nChannel = {after.id}\n```", inline=False)

            await self.channel.send(embed=embed)

        elif before.category != after.category:
            embed = Embed(
             description=f"Text Channel was updated ({after.name})",
             color=discord.Color.from_rgb(73, 131, 179),
               timestamp = datetime.utcnow())
            embed.add_field(name="Created on", value=f"<t:{int(after.created_at.timestamp())}:F>", inline=False)
            embed.add_field(name="Category", value=f"Previous: {before.category}\n Now: {after.category}", inline=False)
            embed.add_field(name="ID", value=f"```ini\nChannel = {after.id}\n```", inline=False)

            await self.channel.send(embed=embed)

        elif before.position != after.position:
            embed = Embed(
             description=f"Text Channel was updated ({after.name})",
             color=discord.Color.from_rgb(73, 131, 179),
               timestamp = datetime.utcnow())
            embed.add_field(name="Created on", value=f"<t:{int(after.created_at.timestamp())}:F>", inline=False)
            embed.add_field(name="Position", value=f"Previous: {before.position}\n Now: {after.position}", inline=False)
            embed.add_field(name="ID", value=f"```ini\nChannel = {after.id}\n```", inline=False)

            await self.channel.send(embed=embed)

        elif before.permissions_for(self.everyone) != after.permissions_for(self.everyone):
            embed = Embed(
             description=f"Text Channel was updated ({after.name})",
             color=discord.Color.from_rgb(73, 131, 179),
               timestamp = datetime.utcnow())
            embed.add_field(name="Created on", value=f"<t:{int(after.created_at.timestamp())}:F>", inline=False)
            embed.add_field(name="Permissions", value=f"Previous: {before.permissions_for(self.everyone)}\n Now: {after.permissions_for(self.everyone)}", inline=False)
            embed.add_field(name="ID", value=f"```ini\nChannel = {after.id}\n```", inline=False)

            await self.channel.send(embed=embed)

        elif before.topic != after.topic:
            embed = Embed(
             description=f"Text Channel was updated ({after.name})",
             color=discord.Color.from_rgb(73, 131, 179),
               timestamp = datetime.utcnow())
            embed.add_field(name="Created on", value=f"<t:{int(after.created_at.timestamp())}:F>", inline=False)
            embed.add_field(name="Topic", value=f"Previous: {before.topic}\n Now: {after.topic}", inline=False)
            embed.add_field(name="ID", value=f"```ini\nChannel = {after.id}\n```", inline=False)

            await self.channel.send(embed=embed)

    @Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if before.channel != after.channel:
            if after.channel is None:
                embed = Embed(
                 description=f"{member.mention} left {before.channel.name}",
                 color=discord.Color.from_rgb(73, 131, 179),
                   timestamp = datetime.utcnow())
                embed.add_field(name="Date", value=f"<t:{int(time.time())}:F>", inline=False)
                embed.add_field(name="ID", value=f"```ini\nUser = {member.id}\nChannel = {before.channel.id}\n```", inline=False)
                await self.channel.send(embed=embed)

            else:
                embed = Embed(
                 description=f"{member.mention} joined {after.channel.name}",
                 color=discord.Color.from_rgb(73, 131, 179),
                   timestamp = datetime.utcnow())
                embed.add_field(name="Date", value=f"<t:{int(time.time())}:F>", inline=False)
                embed.add_field(name="ID", value=f"```ini\nUser = {member.id}\nChannel = {after.channel.id}\n```", inline=False)
                await self.channel.send(embed=embed)
    
    @Cog.listener()
    async def on_role_create(self, role):
        embed = Embed(
         description=f"Role created",
         color=discord.Color.from_rgb(73, 131, 179),
           timestamp = datetime.utcnow())
        embed.add_field(name="Name", value=f"{role.name}", inline=False)
        embed.add_field(name="ID", value=f"```ini\nRole = {role.id}\n```", inline=False)
        await self.channel.send(embed=embed)
    
    @Cog.listener()
    async def on_role_delete(self, role):
        embed = Embed(
         description=f"Role deleted",
         color=discord.Color.from_rgb(73, 131, 179),
           timestamp = datetime.utcnow())
        embed.add_field(name="Name", value=f"{role.name}", inline=False)
        embed.add_field(name="ID", value=f"```ini\nRole = {role.id}\n```", inline=False)
        await self.channel.send(embed=embed)

    @Cog.listener()
    async def on_guild_role_update(self, before, after):
        if before.name != after.name:
            embed = Embed(
             title=f"Role \"{after.name}\" was updated",
             color=discord.Color.from_rgb(73, 131, 179),
               timestamp = datetime.utcnow())
            embed.add_field(name="Name", value=f"Previous: {before.name}\n Now: {after.name}", inline=False)
            embed.add_field(name="ID", value=f"```ini\nRole = {after.id}\n```", inline=False)
            await self.channel.send(embed=embed)

        elif before.permissions != after.permissions:
            embed = Embed(
             title=f"Role \"{after.name}\" was updated",
             color=discord.Color.from_rgb(73, 131, 179),
               timestamp = datetime.utcnow())

            changed_perm_set = set(before.permissions) ^ set(after.permissions)
            if len(changed_perm_set) > 0:
                changed_perm = next(iter(changed_perm_set))
                #and then answer
            if changed_perm in after.permissions:
                embed.add_field(name="Permission Added", value=f"{self.plus} {changed_perm[0]}", inline=False)
            else:
                embed.add_field(name="Permission Removed", value=f"{self.minus} {changed_perm[0]}", inline=False)
            await self.channel.send(embed=embed)
        

def setup(bot):
    bot.add_cog(Log(bot))
