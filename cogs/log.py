from discord.ext import commands
from discord.ext.commands import Cog
from discord import Embed, Forbidden
from datetime import datetime

class Log(Cog):
    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_ready(self):
        print('Bot is ready!.')

    
    @Cog.listener()
    async def on_user_update(self, before, after):
        channel=self.bot.get_channel(869849124537778214)
        if before.name != after.name:
            embed = Embed(title="Member Update",
             description=f"{after.name}#{after.discriminator}'s Username was changed",
              colour=after.colour,
               timestamp = datetime.utcnow())

            fields = [("Before", before.name, False),
                      ("After", after.name, False)]

            for name, value, inline in fields:
                embed.add_field(name=name, value=value, inline=inline)
            await channel.send(embed=embed)

        if before.avatar_url != after.avatar_url:
            embed = Embed(title="Member Update",
            description=f"{after.name}#{after.discriminator} changed their avatar (New Avatar Below)",
            colour=after.color,
            timestamp = datetime.utcnow())
            embed.set_thumbnail(url=before.avatar_url)
            embed.set_image(url=after.avatar_url)

            await channel.send(embed=embed)

    @Cog.listener()
    async def on_member_update(self, before, after):
        channel=self.bot.get_channel(869849124537778214)
        if before.display_name != after.display_name:
            embed = Embed(title="Member Update",
             description="Nickname was changed",
              colour=after.colour,
               timestamp = datetime.utcnow())

            fields = [("Before", before.display_name, False),
                      ("After", after.display_name, False)]

            for name, value, inline in fields:
                embed.add_field(name=name, value=value, inline=inline)
            await channel.send(embed=embed)

        elif before.avatar_url != after.avatar_url:
            embed = Embed(title="Member Update",
            description="Avatar Change (New Avatar Below",
            colour=after.colour,
            timestamp = datetime.utcnow())
            embed.set_thumbnail(url=before.avatar_url)
            embed.set_image(url=after.avatar_url)

            await channel.send(embed=embed)
    @Cog.listener()
    async def on_message_edit(self, before, after):
        if not after.author.bot:
            pass

    @Cog.listener()
    async def on_message_delete(self, before, after):
        if not after.author.bot:
            pass


def setup(bot):
    bot.add_cog(Log(bot))
