import discord
from discord.ext import commands
from discord.ext.commands import Cog
from discord import Embed, Forbidden
from datetime import datetime
import discord

class Log(Cog):
    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_ready(self):
        print('Bot is ready!.')
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
            embed = Embed(title="Member Update",
             description="Nickname was changed",
              color=discord.Color.from_rgb(73, 131, 179),
               timestamp = datetime.utcnow())

            fields = [("Before", before.display_name, False),
                      ("After", after.display_name, False)]

            for name, value, inline in fields:
                embed.add_field(name=name, value=value, inline=inline)
            await self.channel.send(embed=embed)

        elif before.roles != after.roles:
            embed = Embed(title="Member Update",
             description=f"{after.name}#{after.discriminator}'s Roles were updated",
              color=discord.Color.from_rgb(73, 131, 179),
               timestamp = datetime.utcnow())
            
            fields = [("Before", ", ".join([r.mention for r in before.roles]), False),
                      ("After", ", ".join([r.mention for r in after.roles]), False)]

            for name, value, inline in fields:
                embed.add_field(name=name, value=value, inline=inline)
            await self.channel.send(embed=embed)

    @Cog.listener()
    async def on_message_edit(self, before, after):
        if not after.author.bot:
            if before.content != after.content:
                embed = Embed(title=f"Message Edited in #{after.channel}",
             description=f"**Before:** {before.content} \n **After: ** {after.content}",
             color=discord.Color.from_rgb(73, 131, 179),
               timestamp = datetime.utcnow())
                embed.set_author(name=after.author.name, icon_url=after.author.avatar_url)

            await self.channel.send(embed=embed)

    @Cog.listener()
    async def on_message_delete(self, message):
        if not message.author.bot:
            embed = Embed(title=f"Message Deleted in #{message.channel}",
             description=f"{message.content}",
             color=discord.Color.from_rgb(73, 131, 179),
               timestamp = datetime.utcnow())
            embed.set_author(name=message.author.name, icon_url=message.author.avatar_url)
            embed.set_footer(f"ID:{message.id}")        
            await self.channel.send(embed=embed)    
            
            
def setup(bot):
    bot.add_cog(Log(bot))
