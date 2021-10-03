#!python

import discord
from discord.ext import commands
import random
import time
import asyncio
import praw
from discord_slash import SlashCommand, SlashContext

intents = discord.Intents.default()
intents.members = True


custom_prefixes = {}
default_prefixes = "="

async def determine_prefix(bot, message):
    guild = message.guild
    if guild:
        return custom_prefixes.get(guild.id, default_prefixes)
    else:
        return default_prefixes

client = commands.Bot(command_prefix=determine_prefix,
                      help_command=None,
                      case_insensitive=True,
                      intents=intents)

slash = SlashCommand(client, sync_commands=True)

__GID__ = [869849123963162635]

mod_channel = client.get_channel(869849124537778214)


@client.event
async def on_ready():
  print("Bot Online.")
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="over this place ^^"))

@client.command()
@commands.guild_only()
async def setprefix(ctx, *, prefixes=""):
    """Function to change bot prefix from the default

    Args:
        prefixes (str, optional): Prefix to be used. Defaults to "".
    """
    custom_prefixes[ctx.guild.id] = prefixes.split() or default_prefixes
    await ctx.send("Prefixes set!")

@client.event
async def on_message(message):
    welcome = "welcome"
    if welcome.lower() in message.content.lower():
      emoji = client.get_emoji(870303370068520960)
      emoji2 = client.get_emoji(880153476770975754)
      await message.add_reaction(emoji) 
      await message.add_reaction(emoji2)
    await client.process_commands(message)
    
    
@client.command()
async def poll(ctx, x=None, question=None, option1=None, option2=None, option3=None, option4=None, option5=None, option6=None, option7=None, option8=None):
    poll_desc_if_2 = f"""
    ⏱️ The poll ends in **{x} hours**

    🇦 {option1}\n
    🇧 {option2}
    """
    poll_desc_if_3 = f"""
    ⏱️ The poll ends in **{x} hours**

    🇦 {option1}\n
    🇧 {option2}\n
    🇨 {option3}
    """
    poll_desc_if_4 = f"""
    ⏱️ The poll ends in **{x} hours**

    🇦 {option1}\n
    🇧 {option2}\n
    🇨 {option3}\n
    🇩 {option4}
    """
    poll_desc_if_5 = f"""
    ⏱️ The poll ends in **{x} hours**

    🇦 {option1}\n
    🇧 {option2}\n
    🇨 {option3}\n
    🇩 {option4}\n
    🇪 {option5}
    """
    poll_desc_if_6 = f"""
    ⏱️ The poll ends in **{x} hours**

    🇦 {option1}\n
    🇧 {option2}\n
    🇨 {option3}\n
    🇩 {option4}\n
    🇪 {option5}\n
    🇫 {option6}
    """
    poll_desc_if_7 = f"""
    ⏱️ The poll ends in **{x} hours**

    🇦 {option1}\n
    🇧 {option2}\n
    🇨 {option3}\n
    🇩 {option4}\n
    🇪 {option5}\n
    🇫 {option6}\n
    🇬 {option7}
    """
    poll_desc_if_8 = f"""
    ⏱️ The poll ends in **{x} hours**

    🇦 {option1}\n
    🇧 {option2}\n
    🇨 {option3}\n
    🇩 {option4}\n
    🇪 {option5}\n
    🇫 {option6}\n
    🇬 {option7}\n
    🇭 {option8}
    """
    if ctx.author.guild_permissions.administrator:
      if not option1:
        await ctx.send("Use the poll command like this: \n`~~poll {hours you want to run the poll} {question (in quotes)} {choice 1} {choice 2}`, upto 8 choices")
      elif not option2:
        await ctx.send("Use the poll command like this: \n`~~poll {hours you want to run the poll} {question (in quotes)} {choice 1} {choice 2}`, upto 8 choices")
      elif option8:
        polle = discord.Embed(title=question,
                          description=poll_desc_if_8,
                          color=discord.Color.from_rgb(132, 0, 255)
                          )
        polle.set_footer(text=f"Poll ends in {x} hours")
        polle.set_thumbnail(
            url=ctx.author.avatar_url)
        brr = await ctx.send(embed=polle)
        await brr.add_reaction('🇦')
        await brr.add_reaction('🇧')
        await brr.add_reaction('🇨')
        await brr.add_reaction('🇩')
        await brr.add_reaction('🇪')
        await brr.add_reaction('🇫')
        await brr.add_reaction('🇬')
        await brr.add_reaction('🇭')
        await ctx.message.delete()
        hour = int(x)*3600
        await asyncio.sleep(int(hour))
        await ctx.send("Time up! The poll is now closed.")
      elif option7:
        polle = discord.Embed(title=question,
                          description=poll_desc_if_7,
                          color=discord.Color.from_rgb(132, 0, 255)
                          )
        polle.set_thumbnail(
            url=ctx.author.avatar_url)
        brr = await ctx.send(embed=polle)
        await brr.add_reaction('🇦')
        await brr.add_reaction('🇧')
        await brr.add_reaction('🇨')
        await brr.add_reaction('🇩')
        await brr.add_reaction('🇪')
        await brr.add_reaction('🇫')
        await brr.add_reaction('🇬')
        await ctx.message.delete()
        hour = int(x)*3600
        await asyncio.sleep(int(hour))
        await ctx.send("Time up! The poll is now closed.")
      elif option6:
        polle = discord.Embed(title=question,
                          description=poll_desc_if_6,
                          color=discord.Color.from_rgb(132, 0, 255)
                          )
        polle.set_thumbnail(
            url=ctx.author.avatar_url)
        brr = await ctx.send(embed=polle)
        await brr.add_reaction('🇦')
        await brr.add_reaction('🇧')
        await brr.add_reaction('🇨')
        await brr.add_reaction('🇩')
        await brr.add_reaction('🇪')
        await brr.add_reaction('🇫')
        await ctx.message.delete()
        hour = int(x)*3600
        await asyncio.sleep(hour)
        await ctx.send("Time up! The poll is now closed.")
      elif option5:
        polle = discord.Embed(title=question,
                          description=poll_desc_if_5,
                          color=discord.Color.from_rgb(132, 0, 255)
                          )
        polle.set_thumbnail(
            url=ctx.author.avatar_url)
        brr = await ctx.send(embed=polle)
        await brr.add_reaction('🇦')
        await brr.add_reaction('🇧')
        await brr.add_reaction('🇨')
        await brr.add_reaction('🇩')
        await brr.add_reaction('🇪')
        await ctx.message.delete()
        hour = int(x)*3600
        await asyncio.sleep(int(hour))
        await ctx.send("Time up! The poll is now closed.")
      elif option4:
        polle = discord.Embed(title=question,
                          description=poll_desc_if_4,
                          color=discord.Color.from_rgb(132, 0, 255)
                          )
        polle.set_thumbnail(
            url=ctx.author.avatar_url)
        brr = await ctx.send(embed=polle)
        await brr.add_reaction('🇦')
        await brr.add_reaction('🇧')
        await brr.add_reaction('🇨')
        await brr.add_reaction('🇩')
        await ctx.message.delete()
        hour = int(x)*3600
        await asyncio.sleep(int(hour))
        await ctx.send("Time up! The poll is now closed.")
        
      elif option3:
        polle = discord.Embed(title=question,
                          description=poll_desc_if_3,
                          color=discord.Color.from_rgb(132, 0, 255)
                          )
        polle.set_thumbnail(
            url="https://5.imimg.com/data5/CR/NA/II/SELLER-55766215/designer-garden-lighting-pole-500x500.jpg")
        brr = await ctx.send(embed=polle)
        await brr.add_reaction('🇦')
        await brr.add_reaction('🇧')
        await brr.add_reaction('🇨')
        await ctx.message.delete()
        hour = int(x)*3600
        await asyncio.sleep(hour)
        await ctx.send("Time up! The poll is now closed.")
        
      else:
        polle = discord.Embed(title=question,
                          description=poll_desc_if_2,
                          color=discord.Color.from_rgb(132, 0, 255)
                          )
        polle.set_thumbnail(
            url=ctx.author.avatar_url)
        brr = await ctx.send(embed=polle)
        await brr.add_reaction('🇦')
        await brr.add_reaction('🇧')
        await ctx.message.delete()
        hour = int(x)*3600
        await asyncio.sleep(int(hour))
        await ctx.send("Time up! The poll is now closed.")
    else:
        await ctx.send("Sorry you don't have permission to run that command.")

    
@client.command(name='ancn')
async def anon_conf(ctx, arg=None):
    brr = ctx.author.id
    if arg == "help":
        pk = await ctx.send("Make an anonymous confession with this command.")
        time.sleep(3)
        await ctx.message.delete()
        await pk.delete()
    else:
        ak = await ctx.send("Check your DMs <a:hart:872760086790012978> ")
        conf = discord.Embed(description="Anonymous vent/confession here")
        conf.set_footer(text="or type cancel to cancel")
        await ctx.author.send(embed=conf)
        await ctx.message.delete()
        await ak.delete()
        try:
            msg = await client.wait_for('message', check=lambda m: m.author == ctx.author, timeout=300.0)
            if brr != msg.author.id:
                pass
            else:
                cancel = "cancel"
                if cancel.lower() in msg.content.lower():
                    await msg.channel.send("Cancelled.")
                else:
                    vent_embed = discord.Embed(title="Your vent confession",
                                               description=msg.content)
                    vent_channel = client.get_channel(869849125087240204)
                    await vent_channel.send(embed=vent_embed)
                    await msg.channel.send("It was sent to the server <3")
                    morsh = client.get_channel(881951830622498826)
                    embed = discord.Embed(title="Conf Log",
                                               description=f"{msg.author} was the author.")
                    vent_channel = client.get_channel(869849125087240204)
                    await morsh.send(embed=embed)
        except asyncio.TimeoutErrorz:
            await ctx.send("Ouch you ignored me :(")
   

@slash.slash(
    name="staff",
    description="Displays the Staff list.",
    guild_ids=__GID__
)
async def staff(ctx: SlashContext):
    embed = discord.Embed(title="Staff",
                          color=discord.Color.from_rgb(73, 131, 179))
    embed.add_field(name="Owner", value="<@803964694972596274>", inline=False)
    embed.add_field(name="Admin", value="<@613789929134227465>", inline=False)
    embed.add_field(name="Moderators", value="<@875582711073484941>\n<@840627967696830485>\n<@797056468594458637>\n<@705205126390087710>", inline=False)
    embed.add_field(name="Event Managers", value="<@816623527896940604>\n<@821735484715434015>\n<@776912755483607100>", inline=False)
    embed.set_footer(text=f"Applications Closed Currently")
    embed.set_thumbnail(url=ctx.guild.icon_url)
    await ctx.send(embed=embed)



staffs = """
**Owner**


**Admins**



**Moderators**


**Event Managers**

"""


@client.command()
async def report(ctx, user: discord.User, *, args):
  channel = client.get_channel(869849124537778215)
  reporte = discord.Embed(title="User Reported",
                          description=f"{user} was reported by {ctx.author} \n **Reason**\n {args}",
                          color=discord.Color.from_rgb(73, 131, 179))
  await channel.send(embed=reporte)
  await ctx.send("User reported, check your DMs!")
  await ctx.author.send("The user was reported! Dm a staff in detail if you would like :D")
  await ctx.message.delete()

Rules = """
<a:heartarrow:880131099559358525> No Swearing.

<a:heartarrow:880131099559358525> You cannot reveal any personal information in this server like credit cards, phone numbers address, and the rest.

<a:heartarrow:880131099559358525> Please respect everyone in this server.

<a:heartarrow:880131099559358525> No Racism or sexism allowed in this server (it results to instant ban).

<a:heartarrow:880131099559358525> No NUDES.

<a:heartarrow:880131099559358525> Don't ping anyone in this server if unnecessary.

<a:heartarrow:880131099559358525> Don't spam unless its an spam channel.

<a:heartarrow:880131099559358525> If a fight happens between you and an member take it to your own DMs this is a SAFE HAVEN no one needs beef in this server. Please dont start a fight.

<a:heartarrow:880131099559358525> Keep the bot commands on <#869849125087240211>:red_circle: , <#869849125401817098>#:white_circle: , <#869849125401817099>:black_circle: , <#869849126102249502> and <#869849126102249508>
Please use the particular channel for the particular thing your doing.

<a:heartarrow:880131099559358525> no sex talks and jokes... I hope we keep things pg as kids are here!
If there's an offensive username or profile photo in this server, you will be asked to change it immediately.

<a:heartarrow:880131099559358525> Don't spam ping someone.

<a:heartarrow:880131099559358525> keep it in the basic language- English. Try not using any other languages.

<a:heartarrow:880131099559358525> Please don't do anything that makes people uncomfortable.

<a:heartarrow:880131099559358525> Don't harass anyone. Both members and staff members.
They have been chosen through thorough discussion and fair&square.

<a:heartarrow:880131099559358525> Any user with no pfps, they will be asked to add one, if they dont, a direct kick.


3 strikes law and here's how it goes:
1. First Warning, 1 day Mute
2. Second Warning, 1 day Ban
3. Third Warning, Permanent Ban and Kick

If you guys have any complains or suggestions, you can dm any mod or admin online. We will try fixing the problem or look into your suggestions. Or if it is okay to share, do use the <#869849124856541191> channel for it.
If anyone is breaking the rules, please take a screen shot and report them using the =report command

I hope you stay and enjoy!!!
Thank you on behalf of the Owner, Admins and Mods. <:heartu:870286031822405633>
"""

@client.command()
async def rules(ctx):
    embed = discord.Embed(title="Rules",
                          description=Rules,
                          timestamp=ctx.message.created_at,
                          color=discord.Color.from_rgb(73, 131, 179))
    embed.set_footer(text=f"Requested by {ctx.author.name}")
    await ctx.send(embed=embed)
    await ctx.message.delete()


@client.command()
async def mute(ctx, member: discord.Member, *, reason=None):
    if ctx.author.guild_permissions.administrator:
        mod_channel = client.get_channel(869849124537778214)
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
        embed = discord.Embed(title="muted",
                              description=f"{member.mention} was muted ",
                              color=discord.Color.from_rgb(73, 131, 179))
        embed.add_field(name="reason:", value=reason, inline=False)
        await mod_channel.send(embed=embed)
        await ctx.message.delete()
        await member.add_roles(mutedRole, reason=reason)
        await member.send(
            f" you have been muted from: {guild.name} reason: {reason}")

    else:
      await ctx.send("Come back with admin permissions ^-^")


@client.command(name="dm")
async def dm(ctx, message, *users: discord.User):
    for user in users:
        await user.send(message)
        print("sent")


@client.command()
async def ban(ctx, user: discord.Member, *, reason="No reason provided"):
  if ctx.author.guild_permissions.administrator:
    mod_channel = client.get_channel(869849124537778214)
    await user.ban(reason=reason)
    ban = discord.Embed(
        title=f"Banned {user.name}!",
        description=f"Reason: {reason}\nBy: {ctx.author.mention}",
        color=discord.Color.from_rgb(73, 131, 179))
    await mod_channel.send(embed=ban)
    await ctx.send("User Banned.")
    await user.send(embed=ban)
    await ctx.message.delete()
  else:
    await ctx.send("Come back with admin permissions ^-^")


@client.command(aliases=(['8ball']))
async def _8ball(ctx):
    responses = [
        'No.',
        'I think not.',
        'Sure!',
        'Probably.',
        'Of course',
        'My reply is no.',
        'It is certain.',
        'It is decidedly so.',
        'Definitely.',
        'As i see it, yeaa.',
        'Yes',
        'Def',
        'No',
        'um yeah why not?',
        'Some things are best left unknown',
        'I cannot say for now.',
        'My reply is yes.',
        'Duh',
        'My sources say yes.',
        'yep']

    await ctx.send(f'{random.choice(responses)}')


@client.command()
async def kick(ctx, user: discord.Member, *, reason="No reason provided"):
  if ctx.author.guild_permissions.administrator:
    mod_channel = client.get_channel(869849124537778214)
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


reddit = praw.Reddit(
    client_id='mCDj4NrF7pu-LQ',
    client_secret='zMKc1nrYfQl8jGqvg60VOuQAcYb0kg',
    user_agent=
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41',
    check_for_async=False)


@client.command(aliases=(['reddit', 'rd']))
async def _reddit(ctx, *, arg=None):
    if arg:
        memes_submissions = reddit.subreddit(f'{arg}').hot()
        post_to_pick = random.randint(1, 50)
        for i in range(0, post_to_pick):
            mango = next(x for x in memes_submissions if not x.stickied)
            titlee = mango.title
            updoot = mango.score

        if mango.over_18:
            embed = discord.Embed(title="Bonk go to horny jail",
                                  color=discord.Color.from_rgb(73, 131, 179))
            embed.set_footer(text=f"Requested by {ctx.author.name}")
            embed.set_image(
                url=
                "https://i.kym-cdn.com/entries/icons/original/000/033/758/Screen_Shot_2020-04-28_at_12.21.48_PM.png"
            )
            await ctx.send(embed=embed)

        elif mango.is_self:
            await ctx.send(f"**{mango.title}**\n{mango.selftext}")

        
        elif mango.domain != 'i.redd.it':
            await ctx.send("That was a video <:sadge:870298459993948210>")


        else:
            embed = discord.Embed(title=titlee,
                                  color=discord.Color.from_rgb(73, 131, 179))
            embed.set_footer(
                text=f"{updoot}⬆️  | Requested by {ctx.author.name}")
            embed.set_image(url=mango.url)
            await ctx.send(embed=embed)

    else:
        await ctx.send("usage: `~~reddit {subreddit}`")



help_desc = "Under Dev :/"


@slash.slash(
    name="help",
    description="Displays the Basic Commands",
    guild_ids=__GID__
)
async def help(ctx: SlashContext):
    help = discord.Embed(title="Commands",
                         #description="Hi there! My prefix is `=`",
                         description = help_desc,
                         color=discord.Color.from_rgb(73, 131, 179))
    help.add_field(name="Moderation", value=help_desc)
    await ctx.send(embed=help)

    
@client.command()
async def editrules(ctx, msg_id = None, channel: discord.TextChannel = None, *, args=None):
    msg = await channel.fetch_message(msg_id)
    mod_channel = client.get_channel(869849124537778214)
    rulesnew = discord.Embed(title="Rules",
                          description=f"""{args}""",
                          timestamp=ctx.message.created_at,
                          color=discord.Color.from_rgb(73, 131, 179))
    rulesnew.set_footer(text=f"Requested by {ctx.author.name}")
    await msg.edit(embed=rulesnew)
    await ctx.mod_channel("Rules edited.")
    await ctx.message.delete()


part_desc="""
• DM any staff.
• If your server has under 100 members pinging everyone is absolutely necessary.
• The server shouldn't encourage raiding/disruptive behaviour and shouldn't be based around NSFW content.
• If your invite link expires we will delete your server ad unless you reach out to us with a new working invite link.
"""


@client.command()
async def embed(ctx, titlee, *, descriptions):
  template = discord.Embed(title=f"{titlee}",
                          description=descriptions,
                          timestamp=ctx.message.created_at,
                          color=discord.Color.from_rgb(73, 131, 179))
  await ctx.send(embed=template)
  await ctx.message.delete()

client.load_extension("cogs.log")
client.load_extension("cogs.welcome")
client.load_extension("cogs.music")
client.load_extension("cogs.reminder")
client.load_extension("cogs.giveaway")
client.load_extension("cogs.image")
client.run('ODc5NjI0OTcwNDkyMzI1OTM4.YSSclw.H9-hcHYoJOHFZOxln4485_Tlkgc')
