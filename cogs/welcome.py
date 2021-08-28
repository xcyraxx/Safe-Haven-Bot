from discord.ext.commands import Cog
from discord.ext import commands
import discord


class Welcome(Cog):
    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_ready(self):
        print("Welcome up!")

    @Cog.listener()
    async def on_member_join(self, member):
        welcome_mesej = f"""
Heyo! Welcome {member.mention}^^<:yay:870286126085189672>

Our server is a place where you will feel safe! We play with the bots, listen to music, watch movies together and most importantly get to know each other and have fun! We also have different fandoms which you may like! <a:qblob_happy:880153476770975754>

<:check:880300080639385601> check out:
<a:sparkly:880300039870775306> | <#869849124537778208>
<a:sparkly:880300039870775306> | <#872748526759735367>
<a:sparkly:880300039870775306> | <#869849124537778207>
<a:sparkly:880300039870775306> | <#869849124537778209>

And the most important thing... Enjoy!! <a:heart:872760086790012978>
"""
        ment = member.mention
        channel = self.bot.get_channel(869849124537778206)
        notif = self.bot.get_channel(869849124537778214)
        await channel.send(f"Heylo~ {member.mention}")
        embed = discord.Embed(title="°•Welcome to Safe Haven!!•°",
                              description=welcome_mesej,
                              color=discord.Color.from_rgb(73, 131, 179))
        embed.set_image(
            url="https://images-ext-2.discordapp.net/external/gQYsepLoX2Q7rx6M-enMVY9xJrjpEGuwU5roJvvOhWU/https/c.tenor.com/M2Wt2o220uMAAAAC/welcome-aesthetic.gif")
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/869851937699426324/877162557050322974/unknown.png")
        embed.set_author(name=member.name, icon_url=member.avatar_url)
        await channel.send(embed=embed)
        date_format = "%a, %b %d, %Y @ %I:%M %p"
        notifbed = discord.Embed(title="Member Joined",
                                 description=f"{member.mention} has joined.\n Account created at {member.created_at.strftime(date_format)}",
                                 color=discord.Color.from_rgb(73, 131, 179))
        notifbed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/869851937699426324/877162557050322974/unknown.png")
        notifbed.set_author(name=member.name, icon_url=member.avatar_url)
        await notif.send(embed=notifbed)

    @Cog.listener()
    async def on_member_remove(self, member):
        leave_mesej = "goodbye! it is your wish to come back or not but i hope you stay safe!"
        channel = self.bot.get_channel(869849124537778206)
        notif = self.bot.get_channel(869849124537778214)
        await channel.send(f"{member.mention} has left...")
        embed = discord.Embed(title=leave_mesej,
                          color=discord.Color.from_rgb(73, 131, 179))
        embed.set_image(
            url="https://images-ext-1.discordapp.net/external/In0Mt5Jq5CYuEkn9KrOHfn3O3oPQZ46UcvPYobgyoqI/https/c.tenor.com/EbLL24T8XIgAAAAC/aesthetic.gif")
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/869851937699426324/877162557050322974/unknown.png")
        embed.set_author(name=member.name, icon_url=member.avatar_url)
        await channel.send(embed=embed)
        date_format = "%a, %b %d, %Y @ %I:%M %p"
        notifbed = discord.Embed(title="Member Left",
                                 description=f"{member.mention} has left the server.\n Account created at {member.joined_at.strftime(date_format)}",
                                 color=discord.Color.from_rgb(73, 131, 179))
        notifbed.set_author(name=member.name, icon_url=member.avatar_url)
        await notif.send(embed=notifbed)


def setup(bot):
    bot.add_cog(Welcome(bot))
