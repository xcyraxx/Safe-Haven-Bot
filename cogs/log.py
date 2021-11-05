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
            description=f"{after.name}#{after.discriminator} changed their avatar (New Avatar Below)",
            color=discord.Color.from_rgb(73, 131, 179),
            timestamp = datetime.utcnow())
            embed.set_thumbnail(url=before.avatar_url)
            embed.set_image(url=after.avatar_url)

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
                description=f"{after.mention} updated their roles.",
                color=discord.Color.from_rgb(73, 131, 179),
                timestamp = datetime.utcnow()
                )
            embed.add_field(name="New Roles", value=after.roles, inline=False)
            embed.add_field(name="Old Roles", value=before.roles, inline=False)
            embed.add_field(name="ID", value=f"```ini\nUser = {after.id}\n```", inline=False)
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
    async def on_guild_channel_delete(self, channel):
        embed = Embed(title=f"Channel deleted",
             description=f"**Name: **{channel.name}\n **Category: **{channel.category}",
             color=discord.Color.from_rgb(73, 131, 179),
               timestamp = datetime.utcnow())
        await self.channel.send(embed=embed) 


    @Cog.listener()
    async def on_guild_channel_create(self, channel):
        embed = Embed(title=f"Voice Channel created",
             description=f"**Name: **{channel.name}\n **Category: **{channel.category}\n\n**Role override for @everyone**\n",
             color=discord.Color.from_rgb(73, 131, 179),
               timestamp = datetime.utcnow())
        print(channel.overwrites_for(self.everyone))
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

        

def setup(bot):
    bot.add_cog(Log(bot))
