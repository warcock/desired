import discord
from discord.ext.commands import Bot, has_permissions
from discord import Embed
import os
import asyncio
from discord.utils import get
import random
from discord import user
from discord import message
from discord.activity import Game
from discord.user import User
from discord.ext import commands
from discord import guild
from discord.ext import tasks
from discord import mentions
import datetime
import time


from roblox import Client
client = Client()


# // Variables


botusername = "desired"
prefix = "!"
status1 = "testing"
status2 = "warc"
version = "v2.0.3"
vipserverlink = "invalid"
token = "OTY1OTg3MTUyMjcxOTI1MjQ5.Gyut0v.0_poNyYiRNQbi4dSctTCIum3d8v-XK1gCOyYZ8"


# // Prefix and Status


bot = commands.Bot(command_prefix=f"{prefix}", status=discord.Status.idle,activity=discord.Activity(type=discord.ActivityType.watching, name=f"{status1} // {status2}" , case_insensitive=True, intents=discord.Intents.all()))	


# // Removes help


bot.remove_command('help')


# // Prints bot's info from variables after startup


@bot.event
async def on_ready():
  print(f"logged in as {bot.user} [{bot.user.id}]")
  print(f"prefix - {prefix}")
  print(f"version - {version}")
  print("------")


# // Error handlers


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(color=0x2F3136)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed.add_field(name="**failed**",value="missing argument", inline=False)
        embed.set_footer(text=f"{botusername} is currently at {version}")
        await ctx.message.delete()
        await ctx.send(embed=embed, delete_after=20.0)
    if isinstance(error, commands.MissingRole):
        embed = discord.Embed(color=0x2F3136)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed.add_field(name="**failed**",value="missing perm", inline=False)
        embed.set_footer(text=f"{botusername} is currently at {version}")
        await ctx.message.delete()
        await ctx.send(embed=embed, delete_after=20.0)
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(color=0x2F3136)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed.add_field(name="**failed**",value="command not found", inline=False)
        embed.set_footer(text=f"{botusername} is currently at {version}")
        await ctx.message.delete()
        await ctx.send(embed=embed, delete_after=20.0)
    if isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(color=0x2F3136)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed.add_field(name="**failed**",value=f"user currently on command cooldown ({round(error.retry_after, 2)} seconds left)", inline=False)
        embed.set_footer(text=f"{botusername} is currently at {version}")
        await ctx.message.delete()
        await ctx.send(embed=embed, delete_after=20.0)


# // Commands


# - help


@bot.command()
async def help(ctx):
    embed = discord.Embed(color=0x2F3136)
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.add_field(name=f"**!help**",value="shows this current message", inline=False)
    embed.add_field(name=f"**!extrahelp**",value="sends extra help information", inline=False)
    embed.add_field(name=f"**!embed `text` `title`**",value="sends a embed saying `title` and `text`", inline=False)
    embed.add_field(name=f"**!send `text` `type`**",value="sends a message saying `text` with `type`", inline=False)
    embed.add_field(name=f"**!membercount**",value="shows the member count of the guild", inline=False)
    embed.add_field(name=f"**!ping**",value="sends the bot's latency", inline=False)
    embed.add_field(name=f"**!pdadd `member` `amount`**",value="adds a person to the pending list", inline=False)
    embed.add_field(name=f"**!pdremove `member`**",value="removes a person from the pending list", inline=False)
    embed.add_field(name=f"**!whois `username`**",value="sends information about a roblox user", inline=False)
    embed.add_field(name=f"**!vipserver `key`**",value="sends the vip server link [KEY REQUIRED]", inline=False)
    embed.add_field(name=f"**!loadgp**",value="loads the gamepass list", inline=False)
    embed.add_field(name=f"**!pendannc `amount`**",value="pings pend inside announcement channel telling them you dropped `amount`", inline=False)
    embed.add_field(name=f"**!pendchat `amount`**",value="pings pend inside the current channel telling them you dropped `amount`", inline=False)
    embed.add_field(name=f"**!csub**",value="sends the name of your current subscription", inline=False)
    embed.add_field(name=f"**!wl**",value="upgrades a user's subcsription", inline=False)
    embed.add_field(name=f"**!unwl**",value="removes a user's subscription", inline=False)
    embed.add_field(name=f"**!request `type`** [testing]",value="sends the request type to the owner/droppers [!extrahelp for request types]", inline=False)
    embed.add_field(name=f"**!updatelog**",value="sends all update logs", inline=False)
    embed.add_field(name=f"**!github**",value="sends warcock's github page", inline=False)
    embed.add_field(name=f"**!scripts**",value="sends scripts made/remade by warcock", inline=False)
    embed.set_footer(text=f"{botusername} is currently at {version}")
    await ctx.message.delete()
    await ctx.send(embed=embed, delete_after=20.0)


# - extrahelp


@bot.command()
async def extrahelp(ctx):
    embed = discord.Embed(color=0x2F3136)
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.add_field(name=f"**text type**",value="bold [**bold**], italic [***italic***], crossline [~~crossline~~]", inline=False)
    embed.add_field(name=f"**amount type**",value="1 - 20 mil [dhc amount]", inline=False)
    embed.add_field(name=f"**size type**",value="small [small order], mid [mid order], big [big order]", inline=False)
    embed.add_field(name=f"**request type**",value="order [requests a order], refund [requests a refund], giveaway [requests a drop for a giveaway you won], role add/role remove [sends a request for removing or adding your pend role]", inline=False)
    embed.set_footer(text=f"{botusername} is currently at {version}")
    await ctx.message.delete()
    await ctx.send(embed=embed, delete_after=20.0)
  
  
# - membercount


@bot.command()
async def membercount(ctx):
    embed = discord.Embed(color=0x2F3136)
    guild = ctx.guild
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.add_field(name=f"**membercount**",value=f"`{guild.member_count}` members", inline=False)
    embed.set_footer(text=f"{botusername} is currently at {version}")
    await ctx.message.delete()
    await ctx.send(embed=embed, delete_after=20.0)


# - embed


@bot.command()
async def embed(ctx, reason, content):
        embed = discord.Embed(color=0x2F3136)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed.add_field(name=content,value=reason)
        embed.set_footer(text=f"{botusername} is currently at {version}")
        await ctx.message.delete()
        await ctx.send(embed=embed, delete_after=20.0)
        
# - send


@bot.command()
async def send(ctx, content, reason):
    if reason == "bold":
        embed = discord.Embed(color=0x2F3136)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed.add_field(name=f"this message has been sent by {ctx.author.name}", value="`value; " + content + "`")
        embed.set_footer(text=f"{botusername} is currently at {version}")
        await ctx.send("**" + content + "**", delete_after=20.0)
        await ctx.send(embed=embed, delete_after=5.0)
        await ctx.message.delete()
    if reason == "italic":
        embed = discord.Embed(color=0x2F3136)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed.add_field(name=f"this message has been sent by {ctx.author.name}", value="`value; " + content + "`")
        embed.set_footer(text=f"{botusername} is currently at {version}")
        await ctx.send("***" + content + "***", delete_after=20.0)
        await ctx.send(embed=embed, delete_after=5.0)
        await ctx.message.delete()
    if reason == "crossline":
        embed = discord.Embed(color=0x2F3136)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed.add_field(name=f"this message has been sent by {ctx.author.name}", value="`value; " + content + "`")
        embed.set_footer(text=f"{botusername} is currently at {version}")
        await ctx.send("~~" + content + "~~", delete_after=20.0)
        await ctx.send(embed=embed, delete_after=5.0)
        await ctx.message.delete()


# - rank


@bot.command()
async def csub(ctx):

    # // Role Identifier

    casual = discord.utils.get(ctx.guild.roles, id=972493889573388298)
    bronze = discord.utils.get(ctx.guild.roles, id=972493900214321244)
    gold = discord.utils.get(ctx.guild.roles, id=972493913254428724)
    platinum = discord.utils.get(ctx.guild.roles, id=972493916714725437)
    diamond = discord.utils.get(ctx.guild.roles, id=972493919763980349)

    # // Role Checker

    if casual in ctx.author.roles:
        embed = discord.Embed(color=0x2F3136)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed.add_field(name="**subscription**", value="current subscription - `casual`")
        embed.set_footer(text=f"{botusername} is currently at {version}")
        await ctx.send(embed=embed, delete_after=20.0)
        await ctx.message.delete()  
    if bronze in ctx.author.roles:
        embed1 = discord.Embed(color=0x2F3136)
        embed1.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed1.add_field(name="**subscription**", value="current subscription - `bronze`")
        embed1.set_footer(text=f"{botusername} is currently at {version}")
        await ctx.send(embed=embed1, delete_after=20.0)
        await ctx.message.delete()
    if gold in ctx.author.roles:
        embed2 = discord.Embed(color=0x2F3136)
        embed2.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed2.add_field(name="**subscription**", value="current subscription - `gold`")
        embed2.set_footer(text=f"{botusername} is currently at {version}")
        await ctx.send(embed=embed2, delete_after=20.0)
        await ctx.message.delete()
    if platinum in ctx.author.roles:
        embed3 = discord.Embed(color=0x2F3136)
        embed3.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed3.add_field(name="**subscription**", value="current subscription - `platinum`")
        embed3.set_footer(text=f"{botusername} is currently at {version}")
        await ctx.send(embed=embed3, delete_after=20.0)
        await ctx.message.delete() 
    if diamond in ctx.author.roles:
        embed4 = discord.Embed(color=0x2F3136)
        embed4.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed4.add_field(name="**subscription**", value="current subscription - `diamond`")
        embed4.set_footer(text=f"{botusername} is currently at {version}")
        await ctx.send(embed=embed4, delete_after=20.0)
        await ctx.message.delete()


# - whitelist/unwhitelist


@commands.has_role(905733021817249812)
@bot.command()
async def wl(ctx, content, member: discord.Member):

    # // Role Identifier

    casual = discord.utils.get(ctx.guild.roles, id=972493889573388298)
    bronze = discord.utils.get(ctx.guild.roles, id=972493900214321244)
    gold = discord.utils.get(ctx.guild.roles, id=972493913254428724)
    platinum = discord.utils.get(ctx.guild.roles, id=972493916714725437)
    casual1 = get(member.guild.roles, id=972493889573388298)
    bronze1 = get(member.guild.roles, id=972493900214321244)
    gold1 = get(member.guild.roles, id=972493913254428724)
    platinum1 = get(member.guild.roles, id=972493916714725437)
    diamond1 = get(member.guild.roles, id=972493919763980349)

    if content == "bronze":
            await member.add_roles(bronze1) 
            embed = discord.Embed(color=0x2F3136)
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            embed.add_field(name="**upgraded!**", value=f"{member.name}'s subscription upgraded to // `bronze`")
            embed.set_footer(text=f"{botusername} is currently at {version}")
            embed1 = discord.Embed(color=0x2F3136)
            embed1.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            embed1.add_field(name=f"**upgrade - {member.name}**", value="upgraded to `bronze`!")
            embed1.set_footer(text=f"{botusername} is currently at {version}")
            await ctx.send(embed=embed)
            await bot.get_channel(947808772401790996).send(embed=embed1)
            await ctx.message.delete()  
    if content == "gold":
            await member.add_roles(gold1) 
            embed = discord.Embed(color=0x2F3136)
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            embed.add_field(name="**upgraded!**", value=f"{member.name}'s subscription upgraded to // `gold`")
            embed.set_footer(text=f"{botusername} is currently at {version}")
            embed1 = discord.Embed(color=0x2F3136)
            embed1.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            embed1.add_field(name=f"**upgrade - {member.name}**", value="upgraded to `gold`!")
            embed1.set_footer(text=f"{botusername} is currently at {version}")
            await ctx.send(embed=embed)
            await bot.get_channel(947808772401790996).send(embed=embed1)
            await ctx.message.delete()  
    if content == "platinum":
            await member.add_roles(platinum1) 
            embed = discord.Embed(color=0x2F3136)
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            embed.add_field(name="**upgraded!**", value=f"{member.name}'s subscription upgraded to // `platinum`")
            embed.set_footer(text=f"{botusername} is currently at {version}")
            embed1 = discord.Embed(color=0x2F3136)
            embed1.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            embed1.add_field(name=f"**upgrade - {member.name}**", value="upgraded to `platinum`!")
            embed1.set_footer(text=f"{botusername} is currently at {version}")
            await ctx.send(embed=embed)
            await bot.get_channel(947808772401790996).send(embed=embed1)
            await ctx.message.delete()  
    if content == "diamond":
            await member.add_roles(diamond1) 
            embed = discord.Embed(color=0x2F3136)
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            embed.add_field(name="**upgraded!**", value=f"{member.name}'s subscription upgraded to // `diamond`")
            embed.set_footer(text=f"{botusername} is currently at {version}")
            embed1 = discord.Embed(color=0x2F3136)
            embed1.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            embed1.add_field(name=f"**upgrade - {member.name}**", value="upgraded to `diamond`!")
            embed1.set_footer(text=f"{botusername} is currently at {version}")
            await ctx.send(embed=embed)
            await bot.get_channel(947808772401790996).send(embed=embed1)
            await ctx.message.delete()  


@commands.has_role(905733021817249812)
@bot.command()
async def unwl(ctx, member: discord.Member):

    # // Role Identifier

    casual = discord.utils.get(ctx.guild.roles, id=972493889573388298)
    bronze = discord.utils.get(ctx.guild.roles, id=972493900214321244)
    gold = discord.utils.get(ctx.guild.roles, id=972493913254428724)
    platinum = discord.utils.get(ctx.guild.roles, id=972493916714725437)
    diamond = discord.utils.get(ctx.guild.roles, id=972493919763980349)
    casual1 = get(member.guild.roles, id=972493889573388298)
    bronze1 = get(member.guild.roles, id=972493900214321244)
    gold1 = get(member.guild.roles, id=972493913254428724)
    platinum1 = get(member.guild.roles, id=972493916714725437)
    diamond1 = get(member.guild.roles, id=972493919763980349)

    if casual in ctx.author.roles:
        await member.remove_roles(casual1) 
        embed = discord.Embed(color=0x2F3136)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed.add_field(name=f"**subscription removed - {member.name}**", value=f"`casual` subscription removed")
        embed.set_footer(text=f"{botusername} is currently at {version}")
        await bot.get_channel(947808772401790996).send(embed=embed)
        await ctx.send(embed=embed)
    if bronze in ctx.author.roles:
        await member.remove_roles(bronze1) 
        embed = discord.Embed(color=0x2F3136)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed.add_field(name=f"**subscription removed - {member.name}**", value=f"`bronze` subscription removed")
        embed.set_footer(text=f"{botusername} is currently at {version}")
        await bot.get_channel(947808772401790996).send(embed=embed)
        await ctx.send(embed=embed)
    if gold in ctx.author.roles:
        await member.remove_roles(gold1) 
        embed = discord.Embed(color=0x2F3136)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed.add_field(name=f"**subscription removed - {member.name}**", value=f"`gold` subscription removed")
        embed.set_footer(text=f"{botusername} is currently at {version}")
        await bot.get_channel(947808772401790996).send(embed=embed)
        await ctx.send(embed=embed)
    if platinum in ctx.author.roles:
        await member.remove_roles(platinum1) 
        embed = discord.Embed(color=0x2F3136)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed.add_field(name=f"**subscription removed - {member.name}**", value=f"`platinum` subscription removed")
        embed.set_footer(text=f"{botusername} is currently at {version}")
        await bot.get_channel(947808772401790996).send(embed=embed)
        await ctx.send(embed=embed)
    if diamond in ctx.author.roles:
        await member.remove_roles(diamond1) 
        embed = discord.Embed(color=0x2F3136)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed.add_field(name=f"**subscription removed - {member.name}**", value=f"`diamond` subscription removed")
        embed.set_footer(text=f"{botusername} is currently at {version}")
        await bot.get_channel(947808772401790996).send(embed=embed)
        await ctx.send(embed=embed)


# - pend add [roles and embed]


@commands.has_role(905744455984877608)
@bot.command()
async def pdadd(ctx, member: discord.Member, *, content):
    role_get = get(member.guild.roles, id=906822729456570388)
    await member.add_roles(role_get) 
    embedVar = discord.Embed(color=0x2F3136)
    embedVar.add_field(name=f"**pending**", value=member.mention+" `is in pending for " + content + " dhc!`")
    embedVar.timestamp = datetime.datetime.utcnow()
    embedVar.set_footer(text=f"{botusername} is currently at {version}")
    embedVar.set_thumbnail(url='https://cdn.discordapp.com/icons/905732450150391838/1901bc8d8847cdc3de69476e35d30310.png?size=4096')
    await bot.get_channel(1031539032481599489).send(embed=embedVar)
    embed = discord.Embed(color=0x2F3136)
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.timestamp = datetime.datetime.utcnow()
    embed.add_field(name="**success**", value=member.mention + " `has been added to pending list!`")
    embed.set_thumbnail(url='https://cdn.discordapp.com/icons/905732450150391838/1901bc8d8847cdc3de69476e35d30310.png?size=4096')
    embed.set_footer(text=f"hello!")
    await ctx.send(embed=embed)
    await ctx.message.delete()


# - pend remove [roles]


@commands.has_role(905744455984877608)
@bot.command()
async def pdremove(ctx, member: discord.Member, content):
    role_get = get(member.guild.roles, id=906822729456570388)
    await member.remove_roles(role_get) 
    embed = discord.Embed(color=0x2F3136)
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.add_field(name="**pending**", value=member.mention+" **has been removed from pending roles!**")
    embed.set_thumbnail(url="https://cdn.discordapp.com/icons/905732450150391838/1901bc8d8847cdc3de69476e35d30310.png?size=4096")
    embed.set_footer(text=f"{botusername} is currently at {version}")
    await ctx.send(embed=embed)
    embedVar = discord.Embed(color=0x2F3136)
    embedVar.add_field(name=f"**pending**", value=member.mention+" `has been removed from pending! [pending embed deletion]`")
    embedVar.set_thumbnail(url='https://cdn.discordapp.com/icons/905732450150391838/1901bc8d8847cdc3de69476e35d30310.png?size=4096')
    embedVar.timestamp = datetime.datetime.utcnow()
    embedVar.set_footer(text=f"deleted due to " + content + " , at")
    await bot.get_channel(1031539032481599489).send(embed=embedVar)


# - github


@bot.command()
async def github(ctx):
    embed = discord.Embed(color=0x2F3136)
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.add_field(name="**github**", value="https://github.com/midniqhtowls / https://github.com/midniqhtowls/robloxscripts")
    embed.set_footer(text=f"{botusername} is currently at {version}")
    await ctx.message.delete()
    await ctx.send(embed=embed)


# - scripts


@bot.command()
async def scripts(ctx):
    embed = discord.Embed(color=0x2F3136)
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.add_field(name="**JoinLeaveNotification**", value="**https://github.com/midniqhtowls/robloxscripts/blob/main/JoinLeaveNotification.lua**")
    embed.add_field(name="**DroppedGoalNotifier**", value="**https://github.com/midniqhtowls/robloxscripts/blob/main/DroppedGoalNotifier.lua**")
    embed.add_field(name="**Dahood GUI**", value="**https://github.com/midniqhtowls/robloxscripts/blob/main/ok.lua**")
    embed.set_footer(text=f"{botusername} is currently at {version}")
    await ctx.message.delete()
    await ctx.send(embed=embed)


# - ping


@bot.command()
async def ping(ctx):
    embed = discord.Embed(color=0x2F3136)
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.add_field(name="**ping**", value=f"{round(bot.latency * 1000)} ms")
    embed.set_footer(text=f"{botusername} is currently at {version}")
    await ctx.message.delete()
    await ctx.send(embed=embed)


# - whois


@bot.command()
async def whois(ctx, username):
    user = await client.get_user_by_username(username)
    embed = Embed(title=f"Info for {user.name}", color=0x2F3136)
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.add_field(
        name="Username",
        value="`" + user.name + "`"
    )
    embed.add_field(
        name="Display Name",
        value="`" + user.display_name + "`"
    )
    embed.add_field(
        name="User ID",
        value="`" + str(user.id) + "`"
    )
    embed.add_field(name="Profile Link", value="https://www.roblox.com/users/"+str(user.id)+"/profile", inline=False)
    embed.add_field(
        name="Description",
        value="```" + ((user.description or "No description")) + "```", inline=False
    )
    embed.set_thumbnail(
        url=f"https://www.roblox.com/headshot-thumbnail/image?userId={user.id}&width=420&height=420&format=png"
    )
    await ctx.message.delete()
    await ctx.send(embed=embed, delete_after=20.0)


# - vipserver


@bot.command()
async def vipserver(ctx, content):
    if content == "key":
        embed = discord.Embed(color=0x2F3136)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed.add_field(name="**vip server | ✅**", value=f"{vipserverlink}")
        embed.set_footer(text=f"{botusername} is currently at {version}")
        await ctx.message.delete()
        await ctx.send(embed=embed, delete_after=20.0)
    else:
        embed = discord.Embed(color=0x2F3136)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed.add_field(name="**vip server | ❌**", value="lol u thought")
        embed.set_footer(text=f"{botusername} is currently at {version}")
        await ctx.message.delete()
        await ctx.send(embed=embed, delete_after=20.0)


# - update logs


@bot.command()
async def updatelog(ctx):
    await ctx.message.delete()
    # page 1 [1.0.0-1.0.2]

    page1 = discord.Embed(color=0x2F3136)
    page1.set_author(name="UpdateLog", icon_url=ctx.author.avatar_url)
    page1.add_field(name="**v1.0.0**", value="`[+]` added 6 commands [help, extrahelp, membercount, embed, send, ping]", inline=False)
    page1.add_field(name="**v1.0.1**", value="`[+]` added error handlers", inline=False)
    page1.add_field(name="**v1.0.2**", value="`[/]` bug fixes", inline=False)
    page1.set_footer(text=f"{botusername} is currently at {version}")

    # page 2 [1.0.3-1.0.5]

    page2 = discord.Embed(color=0x2F3136)
    page2.set_author(name="UpdateLog", icon_url=ctx.author.avatar_url)
    page2.add_field(name="**v1.0.3**", value="`[+]` added 2 commands [pdadd, pdremove]", inline=False)
    page2.add_field(name="**v1.0.4**", value="`[+]` added 3 commands [vipserver, whois, loadgp]", inline=False)
    page2.add_field(name="**v1.0.5**", value="`[+]` added 3 commands [pendannc, pendchat, request]", inline=False)
    page2.set_footer(text=f"{botusername} is currently at {version}")

    # page 3 [1.0.6-1.0.8]

    page3 = discord.Embed(color=0x2F3136)
    page3.set_author(name="UpdateLog", icon_url=ctx.author.avatar_url)
    page3.add_field(name="**v1.0.6**", value="`[+]` added 1 command [checksubscription]", inline=False)
    page3.add_field(name="**v1.0.7**", value="`[/]` bug fixes", inline=False)
    page3.add_field(name="**v1.0.8**", value="`[+]` added 1 command [updatelog]", inline=False)
    page3.set_footer(text=f"{botusername} is currently at {version}")

    # page 4 [1.0.9-2.0.1]

    page4 = discord.Embed(color=0x2F3136)
    page4.set_author(name="UpdateLog", icon_url=ctx.author.avatar_url)
    page4.add_field(name="**v1.0.9**", value="`[/]` bug fixes", inline=False)
    page4.add_field(name="**v2.0.0**", value="`[+]` added 2 commands [github, scripts]", inline=False)
    page4.add_field(name="**v2.0.1**", value="`[/]` fixed [checksubscription]", inline=False)
    page4.set_footer(text=f"{botusername} is currently at {version}")

    # page 5 [2.0.2-2.0.4]

    page5 = discord.Embed(color=0x2F3136)
    page5.set_author(name="UpdateLog", icon_url=ctx.author.avatar_url)
    page5.add_field(name="**v2.0.2**", value="`[+]` added 2 commands [wl, unwl]", inline=False)
    page5.add_field(name="**v2.0.3**", value="`[+]` added more pages to [loadgp]", inline=False)
    page5.add_field(name="**v2.0.4**", value="`[-]` ||unreleased||", inline=False)
    page5.set_footer(text=f"{botusername} is currently at {version}")

    bot.help_pages = [page1, page2, page3, page4, page5]

    buttons = [u"\u23EA", u"\u25C0", u"\u25B6", u"\u23E9"]
    current = 0
    msg = await ctx.send(embed=bot.help_pages[current])

    for button in buttons:
        await msg.add_reaction(button)
    while True:
        try:
            reaction, user = await bot.wait_for("reaction_add", check=lambda reaction, user: user == ctx.author and reaction.emoji in buttons)

        except asyncio.TimeoutError:
            embed = bot.help_pages[current]
            embed.set_footer(text="20a4795pg71c0711e-71c0711")
            await msg.clear_reactions()

        else:
            previous_page = current

            if reaction.emoji == "\u23EA":
                current = 0

            elif reaction.emoji == u"\u25C0":
                if current > 0:
                    current -= 1

            elif reaction.emoji == u"\u25B6":
                if current < len(bot.help_pages)-1:
                    current +=1

            elif reaction.emoji == u"\u23E9":
                current = len(bot.help_pages)-1

            for button in buttons:
                await msg.remove_reaction(button, ctx.author)

            if current != previous_page:
                await msg.edit(embed=bot.help_pages[current])


# - gamepass embed loader


@bot.command()
async def loadgp(ctx):
    await ctx.message.delete()
    # page 1 [1-5]

    page1 = discord.Embed(color=0x2F3136)
    page1.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    page1.add_field(name="**1 mil**", value="https://www.roblox.com/game-pass/23106641/1-mil-dhc", inline=False)
    page1.add_field(name="**2 mil**", value="https://www.roblox.com/game-pass/23106651/2-mil-dhc", inline=False)
    page1.add_field(name="**3 mil**", value="https://www.roblox.com/game-pass/23106656/3-mil-dhc", inline=False)
    page1.add_field(name="**4 mil**", value="https://www.roblox.com/game-pass/23106660/4-mil-dhc", inline=False)
    page1.add_field(name="**5 mil**", value="https://www.roblox.com/game-pass/23106667/5-mil-dhc", inline=False)
    page1.set_footer(text=f"{botusername} is currently at {version}")

    # page 2 [6-10]

    page2 = discord.Embed(color=0x2F3136)
    page2.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    page2.add_field(name="**6 mil**", value="https://www.roblox.com/game-pass/23106709/6-mil-dhc", inline=False)
    page2.add_field(name="**7 mil**", value="https://www.roblox.com/game-pass/23106710/7-mil-dhc", inline=False)
    page2.add_field(name="**8 mil**", value="https://www.roblox.com/game-pass/23106717/8-mil-dhc", inline=False)
    page2.add_field(name="**9 mil**", value="https://www.roblox.com/game-pass/23106730/9-mil-dhc", inline=False)
    page2.add_field(name="**10 mil**", value="https://www.roblox.com/game-pass/23106731/10-mil-dhc", inline=False)
    page2.set_footer(text=f"{botusername} is currently at {version}")

    # page 3 [11-15]

    page3 = discord.Embed(color=0x2F3136)
    page3.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    page3.add_field(name="**placeholder**", value="placeholder", inline=False)
    page3.add_field(name="**placeholder**", value="placeholder", inline=False)
    page3.add_field(name="**placeholder**", value="placeholder", inline=False)
    page3.add_field(name="**placeholder**", value="placeholder", inline=False)
    page3.add_field(name="**15 mil**", value="https://www.roblox.com/game-pass/23106746/15-mil-dhc", inline=False)
    page3.set_footer(text=f"{botusername} is currently at {version}")

    # page 4 [16-20]

    page4 = discord.Embed(color=0x2F3136)
    page4.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    page4.add_field(name="**placeholder**", value="placeholder", inline=False)
    page4.add_field(name="**placeholder**", value="placeholder", inline=False)
    page4.add_field(name="**placeholder**", value="placeholder", inline=False)
    page4.add_field(name="**placeholder**", value="placeholder", inline=False)
    page4.add_field(name="**20 mil**", value="https://www.roblox.com/game-pass/23106737/20-mil-dhc", inline=False)
    page4.add_field(name="**perma fp**", value="https://www.roblox.com/game-pass/23106537/perma-fast-pass", inline=False)
    page4.add_field(name="**otfp [1]**", value="https://www.roblox.com/game-pass/23106633/one-time-fast-pass", inline=False)
    page4.add_field(name="**otfp [2]**", value="https://www.roblox.com/game-pass/23106530/one-time-fast-pass-2", inline=False)
    page4.set_footer(text=f"{botusername} is currently at {version}")

    # page 5 [subscriptions]

    page5 = discord.Embed(color=0x2F3136)
    page5.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    page5.add_field(name="**casual**", value="free", inline=False)
    page5.add_field(name="**bronze**", value="https://www.roblox.com/game-pass/85614118/bronze", inline=False)
    page5.add_field(name="**gold**", value="https://www.roblox.com/game-pass/85614187/gold", inline=False)
    page5.add_field(name="**platinum**", value="https://www.roblox.com/game-pass/85614234/platinum", inline=False)
    page5.add_field(name="**diamond**", value="https://www.roblox.com/game-pass/85614285/diamond", inline=False)
    page5.add_field(name="**placeholder**", value="placeholder", inline=False)
    page5.add_field(name="**placeholder**", value="placeholder", inline=False)
    page5.add_field(name="**placeholder**", value="placeholder", inline=False)
    page5.set_footer(text=f"{botusername} is currently at {version}")

    bot.help_pages = [page1, page2, page3, page4, page5]

    buttons = [u"\u23EA", u"\u25C0", u"\u25B6", u"\u23E9"]
    current = 0
    msg = await ctx.send(embed=bot.help_pages[current])

    for button in buttons:
        await msg.add_reaction(button)
    while True:
        try:
            reaction, user = await bot.wait_for("reaction_add", check=lambda reaction, user: user == ctx.author and reaction.emoji in buttons, timeout=60.0)

        except asyncio.TimeoutError:
            embed = bot.help_pages[current]
            embed.set_footer(text="timed Out")
            await msg.clear_reactions()

        else:
            previous_page = current

            if reaction.emoji == "\u23EA":
                current = 0

            elif reaction.emoji == u"\u25C0":
                if current > 0:
                    current -= 1

            elif reaction.emoji == u"\u25B6":
                if current < len(bot.help_pages)-1:
                    current +=1

            elif reaction.emoji == u"\u23E9":
                current = len(bot.help_pages)-1

            for button in buttons:
                await msg.remove_reaction(button, ctx.author)

            if current != previous_page:
                await msg.edit(embed=bot.help_pages[current])


# - pend mention [for droppers]


@commands.has_role(917021208803938314)
@commands.cooldown(1, 1800, commands.BucketType.user)
@bot.command()
async def pendannc(ctx, content):
        embed = discord.Embed(color=0x2F3136)
        embed.add_field(name="**pend**", value=f"{ctx.author.name} has dropped {content}, ping them inside your ticket to claim your order")
        embed.set_footer(text=f"{botusername} is currently at {version}")
        await ctx.message.delete()
        await bot.get_channel(905791426045046794).send("<@&905744463874379777>", embed=embed)


@commands.has_role(917021208803938314)
@commands.cooldown(1, 1800, commands.BucketType.user)
@bot.command()
async def pendchat(ctx, content):
        await ctx.message.delete()
        await ctx.send(f"<@&905744463874379777> {ctx.author.name} has dropped {content}, ping them inside your ticket to claim your order")


# - run


@commands.has_role(917021208803938314)
@bot.command()
async def run(ctx, int, content):
        await ctx.message.delete()
        embed = discord.Embed(color=0x2F3136)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed.add_field(name="desired", value="restarting the bot!")
        embed.add_field(name="version", value=int)
        embed.add_field(name="due to", value=content)
        embed.set_footer(text=f"this can take up to a minute!")
        await ctx.send(embed=embed, delete_after=20.0)
        await ctx.message.delete()

  
# - request 


@bot.command()
async def request(ctx, reason, content):
    if reason == "order":
        embed = discord.Embed(color=0x2F3136)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed.add_field(name=f"request - order", value="drop request for "+ content +" mil sent")
        embed.set_footer(text=f"{botusername} is currently at {version}")
        await ctx.send(embed=embed, delete_after=20.0)
        await ctx.message.delete()
    elif reason == "refund":
        embed1 = discord.Embed(color=0x2F3136)
        embed1.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed1.add_field(name=f"request - refund", value="refund request for "+ content +" robux sent")
        embed1.set_footer(text=f"{botusername} is currently at {version}")
        await ctx.send(embed=embed1, delete_after=20.0)
        await ctx.message.delete()
    elif reason == "giveaway":
        embed2 = discord.Embed(color=0x2F3136)
        embed2.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed2.add_field(name=f"request - giveaway", value="giveaway drop request for "+ content +" mil sent")
        embed2.set_footer(text=f"{botusername} is currently at {version}")
        await ctx.send(embed=embed2, delete_after=20.0)
        await ctx.message.delete()
    elif reason == "role":
        embed3 = discord.Embed(color=0x2F3136)
        embed3.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed3.add_field(name=f"request - role", value="role "+ content +" request sent")
        embed3.set_footer(text=f"{botusername} is currently at {version}")
        await ctx.send(embed=embed3, delete_after=20.0)
        await ctx.message.delete()
    else:
        await ctx.send("invalid")


#------------#

bot.run(token)

#------------#
