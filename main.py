#!python

import discord
from discord.ext import commands
import random
from discord.flags import Intents
import praw


intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix='~~',
                      help_command=None,
                      case_insensitive=True,
                      intents=intents)

mod_channel = client.get_channel(869849124537778214)

@client.event
async def on_ready():
  print("Bot Online.")
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="over this place ^^"))


@client.event
async def on_message(message):
    welcome = "welcome"
    if client.user.mentioned_in(message):
        await message.channel.send("You can type `~~help` for more info")
    elif welcome.lower() in message.content.lower():
      emoji = client.get_emoji(870303370068520960)
      emoji2 = client.get_emoji(880153476770975754)
      await message.add_reaction(emoji) 
      await message.add_reaction(emoji2)
    await client.process_commands(message)

    
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
        except asyncio.TimeoutErrorz:
            await ctx.send("Ouch you ignored me :(")
   

@client.command()
async def staff(ctx):
    embed = discord.Embed(title="Staff",
                          description=staffs,
                          timestamp=ctx.message.created_at,
                          color=discord.Color.from_rgb(73, 131, 179))
    embed.set_footer(text=f"Requested by {ctx.author.name}")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/869851937699426324/877162557050322974/unknown.png")
    await ctx.send(embed=embed)


@client.command()
async def stats(ctx):
  member_count = len(ctx.guild.members)
  true_member_count = len([m for m in ctx.guild.members if not m.bot])
  bot_count = len([m for m in ctx.guild.members if m.bot])
  embed = discord.Embed(title='Members',
                          description=f"Total Members: {member_count} \nMembers: {true_member_count} \nBots: {bot_count}",
                          timestamp=ctx.message.created_at,
                          color=discord.Color.from_rgb(73, 131, 179))
  embed.set_footer(text=f"^-^")
  await ctx.send(embed=embed)


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
1. Warning 1 ban for 1 day.
2. Warning 2 ban for 2 weeks.
3. Warning 3 permanent ban.
If you guys have any complains or suggestions, you can dm any mod or admin online. We will try fixing the problem or look into your suggestions. Or if it is okay to share, do use the <#869849124856541191> channel for it.
If anyone is breaking the rules, please take a screen shot and ping a staff member!!
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


staffs = """
**Owner**

<@803964694972596274>

**Admins**

<@875582711073484941>

**Moderators**

<@837703622896386149>
<@730347343265661009>
<@840627967696830485>
<@797056468594458637>
<@705205126390087710>
<@613789929134227465>
<@869917928164835338>
<@797056468594458637>

**Event Managers**

<@816623527896940604>
<@814580128200785950>
"""


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


@client.command(aliases=(['um']))
async def unmute(ctx, user: discord.User):
  if ctx.author.guild_permissions.manage_roles:
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    if ctx.author.guild_permissions.administrator:
        await user.remove_roles(role)
        embed = discord.Embed(title="Unmuted",
                              description=f"{user.mention} was unmuted ",
                              color=discord.Color.from_rgb(73, 131, 179))
        await ctx.send(embed=embed)
        await ctx.message.delete()


@client.command(name="dm")
async def dm(ctx, message, *users: discord.User):
    for user in users:
        await user.send(message)
        print("sent")


@client.command(aliases=(['cr']))
async def createrole(ctx, arg, *, perms=None):
  if ctx.author.guild_permissions.manage_roles:
    mod_channel = client.get_channel(869849124537778214)
    guild = ctx.guild
    await guild.create_role(name=f"{arg}")
    await mod_channel.send(f"Role {arg} was successfully created")
    await ctx.message.delete()
  else:
    await ctx.send("Come back with admin permissions ^-^")


@client.command(aliases=(['ar']))
async def giverole(ctx, role: discord.Role, user: discord.Member):
    mod_channel = client.get_channel(869849124537778214)
    if ctx.author.guild_permissions.manage_roles:
        await user.add_roles(role)
        await mod_channel.send(f"Role {role} was successfully added to {user}")
        await ctx.message.delete()
    else:
      await ctx.send("Come back with admin permissions ^-^")


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
    await user.send(embed=ban)
    await ctx.message.delete()
  else:
    await ctx.send("Come back with admin permissions ^-^")


@client.command(aliases=(['rr']))
async def remove_role(ctx, role: discord.Role, user: discord.Member):
    if ctx.author.guild_permissions.manage_roles:
        mod_channel = client.get_channel(869849124537778214)
        await user.remove_roles(role)
        await mod_channel.send(f"Role {role} was successfully removed from {user}")
        await ctx.message.delete()
    else:
      await ctx.send("Come back with admin permissions ^-^")


reddit = praw.Reddit(
    client_id='mCDj4NrF7pu-LQ',
    client_secret='zMKc1nrYfQl8jGqvg60VOuQAcYb0kg',
    user_agent=
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41',
    check_for_async=False)


@client.command(aliases=(['reddit']))
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
            embed = discord.Embed(title=titlee,
                                  description=mango.selftext,
                                  color=discord.Color.from_rgb(73, 131, 179))
            embed.set_footer(
                text=f"{updoot}⬆️  | Requested by {ctx.author.name}")
            print(mango.selftext)
            await ctx.send(embed=embed)

        
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



help_desc = """
mute,kick,ban,giverole,removerole,createrole,staff,rules,reddit,8ball,dm,stats,report,ancn,embed
`help {command_name}` for more info :D
"""


@client.command()
async def help(ctx, *, arg = None):
    if arg == "help":
      await ctx.send("wut?")
    elif arg == "staff":
      await ctx.send("Shows the list of staff")
    elif arg == "reddit":
      await ctx.send("usage: `~~reddit {subreddit}`  Sends a random post from the mentioned subreddit")
    elif arg == "8ball":
      await ctx.send("usage: `~~8ball {any Yes/No question`  Answers any yes/no question")
    elif arg == "rules":
      await ctx.send("Just the rules....?")
    elif arg == "mute":
      await ctx.send("usage: `~~mute @someone {reason}`")
    elif arg == "kick":
      await ctx.send("usage: `~~kick @someone {reason}`")
    elif arg == "ban":
      await ctx.send("usage: `~~ban @someone {reason}`")
    elif arg == "createrole":
      await ctx.send("usage: `~~createrole/cr {role_name}`  Creates a role with given name")
    elif arg == "removerole":
      await ctx.send("usage: `~~removerole/rr @role @user`  Removes mentioned role from person")
    elif arg == "addrole":
      await ctx.send("usage: `~~giverole/gr @role @user`  Gives mentioned User the role")
    elif arg == "dm":
      await ctx.send("""usage: `~~dm "{anything}" @someone`""" )
    elif arg == "report":
      await ctx.send("usage: `~~report @user {reason}`")
    elif arg == "embed":
      await ctx.send("`~~embed {title} {content}`")
    else:
      help = discord.Embed(title="Commands",
                         description=help_desc,
                         timestamp=ctx.message.created_at,
                         color=discord.Color.from_rgb(73, 131, 179))
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
async def partnership(ctx):
  if ctx.author.guild_permissions.administrator:
    partner = discord.Embed(title="➤ PARTNERSHIP REQUIREMENTS",
                          description=part_desc,
                          color=discord.Color.from_rgb(73, 131, 179))
    partner.set_image(url="https://images-ext-2.discordapp.net/external/yrjUrfJHpCtmENHqKHNfRtNu70B2bDV6WamkIngdW-M/https/images-ext-2.discordapp.net/external/-qqulj4HDYbBszc_kJZuG9aiBrN6GtrI5OmjrJE8pPA/https/c.tenor.com/1E-FiOOEbaYAAAAd/green.gif")
    partner.set_thumbnail(url="https://cdn.discordapp.com/attachments/869851937699426324/877162557050322974/unknown.png")
    await ctx.message.delete()
    await ctx.send (embed=partner) 


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
client.run('ODc5NjI0OTcwNDkyMzI1OTM4.YSSclw.H9-hcHYoJOHFZOxln4485_Tlkgc')
