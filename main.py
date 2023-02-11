import discord
import datetime
from termcolor import colored
from discord import app_commands
from discord.utils import get

intents = discord.Intents.default()
bot = discord.Client(intents=intents,status=discord.Status.idle,activity=discord.Activity(type=discord.ActivityType.watching, name="desired"))
tree = app_commands.CommandTree(bot)

# -----------------------------------------------

class desiredRewrite:
    desiredRewriteV1_ServerID = 883531567551615026
    desiredRewriteV1_RoleRequiredID = 1061629027636490281
    desiredRewriteV1_BotToken = "OTY1OTg3MTUyMjcxOTI1MjQ5.Gyut0v.0_poNyYiRNQbi4dSctTCIum3d8v-XK1gCOyYZ8"
    desiredRewriteV1_Color_Purple = '\033[95m'
    desiredRewriteV1_Color_Cyan = '\033[96m'
    desiredRewriteV1_Color_DarkCyan = '\033[36m'
    desiredRewriteV1_Color_Blue = '\033[94m'
    desiredRewriteV1_Color_Green = '\033[92m'
    desiredRewriteV1_Color_Yellow = '\033[93m'
    desiredRewriteV1_Color_Red = '\033[91m'
    desiredRewriteV1_Text_BoldFont = '\033[1m'
    desiredRewriteV1_Text_UnderlineText = '\033[4m'
    desiredRewriteV1_Text_Color_End = '\033[0m'

# -----------------------------------------------

@tree.command(name = "help", description = "sends a list of commands", guild=discord.Object(id=desiredRewrite.desiredRewriteV1_ServerID))
async def help(interaction: discord.Interaction):
        embed = discord.Embed(color=0x2F3136)
        embed.set_author(name=interaction.user, icon_url=interaction.user.avatar)
        embed.add_field(name=f"**help**",value="sends a list of commands", inline=False)
        embed.add_field(name=f"**membercount**",value="shows the member count of the guild", inline=False)
        embed.add_field(name=f"**ping**",value="sends the bot's latency", inline=False)
        embed.add_field(name=f"**pdadd `member` `amount`**",value="adds a person to the pending list", inline=False)
        embed.add_field(name=f"**pdremove `member`**",value="removes a person from the pending list", inline=False)
        embed.add_field(name=f"**dahood `amount`**",value="loads the gamepass list for dahood cash", inline=False)
        embed.add_field(name=f"**fastpass `type`**",value="loads the gamepass list for fastpasses", inline=False)
        embed.add_field(name=f"**sub `type`**",value="loads the gamepass list for subscriptions", inline=False)
        embed.add_field(name=f"**pendannc `amount`**",value="pings pend inside announcement channel telling them you dropped `amount`", inline=False)
        embed.add_field(name=f"**pendchat `amount`**",value="pings pend inside the current channel telling them you dropped `amount`", inline=False)
        embed.add_field(name=f"**csub**",value="checks your current subscription", inline=False)
        embed.add_field(name=f"**wl**",value="upgrades a user's subcsription", inline=False)
        embed.add_field(name=f"**unwl**",value="removes a user's subscription", inline=False)
        embed.add_field(name=f"**request `type`** [testing]",value="sends the request type to the owner/droppers [!extrahelp for request types]", inline=False)
        embed.add_field(name=f"**updatelog**",value="sends all update logs", inline=False)
        embed.add_field(name=f"**github**",value="sends warcock's github page", inline=False)
        embed.add_field(name=f"**scripts**",value="sends scripts made/remade by warcock", inline=False)
        await interaction.response.send_message(embed=embed)

@tree.command(name = "membercount", description = "shows the total count of members inside the server", guild=discord.Object(id=desiredRewrite.desiredRewriteV1_ServerID))
async def embed(interaction: discord.Interaction):
    embed = discord.Embed(color=0x2F3136)
    guild = interaction.guild
    embed.set_author(name=interaction.user, icon_url=interaction.user.avatar)
    embed.add_field(name=f"**membercount**", value=f"{guild.name} currently has `{guild.member_count}` total members", inline=False)
    await interaction.response.send_message(embed=embed)

@tree.command(name = "ping", description = "sends the bot's latency", guild=discord.Object(id=desiredRewrite.desiredRewriteV1_ServerID))
async def embed(interaction: discord.Interaction):
    embed = discord.Embed(color=0x2F3136)
    embed.set_author(name=interaction.user, icon_url=interaction.user.avatar)
    embed.add_field(name="**ping**", value=f"{round(bot.latency * 1000)} ms")
    await interaction.response.send_message(embed=embed)

@tree.command(name = "pdadd", description = "adds a member to the pending list", guild=discord.Object(id=desiredRewrite.desiredRewriteV1_ServerID))
async def pdadd(interaction: discord.Interaction, member: discord.Member, amount: int):
    bot.role = interaction.guild.get_role(desiredRewrite.desiredRewriteV1_RoleRequiredID)
    if bot.role not in interaction.user.roles:
        await interaction.response.send_message("**`failed`** `//` **`you do not have permission to run this command!`**")
    else:
        desiredRewriteGetRole = get(member.guild.roles, id=1051069786085396520)
        await member.add_roles(desiredRewriteGetRole) 
        embed = discord.Embed(color=0x2F3136)
        embed.set_author(name=interaction.user, icon_url=interaction.user.avatar)
        embed.add_field(name="**pending list add [success]**", value=f"{member} has been added to the pending list! [{amount}m pending]")
        embed.set_thumbnail(url='https://cdn.discordapp.com/icons/905732450150391838/1901bc8d8847cdc3de69476e35d30310.png?size=4096')
        embed.timestamp = datetime.datetime.utcnow()
        await interaction.response.send_message(embed=embed, ephemeral=True)
        embed1 = discord.Embed(color=0x2F3136)
        embed.set_author(name=interaction.user, icon_url=interaction.user.avatar)
        embed1.add_field(name="**pending [add]**", value=f"{member} is now in pending for {amount}m!")
        embed1.set_thumbnail(url='https://cdn.discordapp.com/icons/905732450150391838/1901bc8d8847cdc3de69476e35d30310.png?size=4096')
        embed1.timestamp = datetime.datetime.utcnow()
        await bot.get_channel(1051077757834117200).send(embed=embed1)

@tree.command(name = "pdremove", description = "removes a member from the pending list", guild=discord.Object(id=desiredRewrite.desiredRewriteV1_ServerID))
async def pdremove(interaction: discord.Interaction, member: discord.Member, reason: str):
    bot.role = interaction.guild.get_role(desiredRewrite.desiredRewriteV1_RoleRequiredID)
    if bot.role not in interaction.user.roles:
        await interaction.response.send_message("**`failed`** `//` **`you do not have permission to run this command!`**")
    else:
        desiredRewriteGetRole = get(member.guild.roles, id=1051069786085396520)
        await member.add_roles(desiredRewriteGetRole) 
        embed = discord.Embed(color=0x2F3136)
        embed.set_author(name=interaction.user, icon_url=interaction.user.avatar)
        embed.add_field(name="**pending list remove [success]**", value=f"{member} has been removed the pending list!")
        embed.set_thumbnail(url='https://cdn.discordapp.com/icons/905732450150391838/1901bc8d8847cdc3de69476e35d30310.png?size=4096')
        embed.timestamp = datetime.datetime.utcnow()
        await interaction.response.send_message(embed=embed, ephemeral=True)

@tree.command(name = "dahood", description = "sends the amount of da hood cash you want to buy", guild=discord.Object(id=desiredRewrite.desiredRewriteV1_ServerID))
@app_commands.describe(amount="amount of da hood cash to choose from")
@app_commands.choices(amount=[
    discord.app_commands.Choice(name='1M', value=1),
    discord.app_commands.Choice(name='2M', value=2),
    discord.app_commands.Choice(name='3M', value=3),
    discord.app_commands.Choice(name='4M', value=4),
    discord.app_commands.Choice(name='5M', value=5),
    discord.app_commands.Choice(name='6M', value=6),
    discord.app_commands.Choice(name='7M', value=7),
    discord.app_commands.Choice(name='8M', value=8), 
    discord.app_commands.Choice(name='9M', value=9),
    discord.app_commands.Choice(name='10M', value=10),
    discord.app_commands.Choice(name='15M', value=11),
    discord.app_commands.Choice(name='20M', value=12),
])
async def dahood(interaction: discord.Interaction, amount: discord.app_commands.Choice[int]):
    if amount.value == 1:
        embed = discord.Embed(color=0x2F3136)
        embed.set_author(name=interaction.user, icon_url=interaction.user.avatar)
        embed.add_field(name="**gamepass // dahood**", value=f"https://www.roblox.com/game-pass/23106641/1-mil-dhc")
        await interaction.response.send_message(embed=embed)
    elif amount.value == 2:
        embed = discord.Embed(color=0x2F3136)
        embed.set_author(name=interaction.user, icon_url=interaction.user.avatar)
        embed.add_field(name="**gamepass // dahood**", value=f"https://www.roblox.com/game-pass/23106651/2-mil-dhc")
        await interaction.response.send_message(embed=embed)
    elif amount.value == 3:
        embed = discord.Embed(color=0x2F3136)
        embed.set_author(name=interaction.user, icon_url=interaction.user.avatar)
        embed.add_field(name="**gamepass // dahood**", value=f"https://www.roblox.com/game-pass/23106656/3-mil-dhc")
        await interaction.response.send_message(embed=embed)
    elif amount.value == 4:
        embed = discord.Embed(color=0x2F3136)
        embed.set_author(name=interaction.user, icon_url=interaction.user.avatar)
        embed.add_field(name="**gamepass // dahood**", value=f"https://www.roblox.com/game-pass/23106660/4-mil-dhc")
        await interaction.response.send_message(embed=embed)
    elif amount.value == 5:
        embed = discord.Embed(color=0x2F3136)
        embed.set_author(name=interaction.user, icon_url=interaction.user.avatar)
        embed.add_field(name="**gamepass // dahood**", value=f"https://www.roblox.com/game-pass/23106667/5-mil-dhc")
        await interaction.response.send_message(embed=embed)
    elif amount.value == 6:
        embed = discord.Embed(color=0x2F3136)
        embed.set_author(name=interaction.user, icon_url=interaction.user.avatar)
        embed.add_field(name="**gamepass // dahood**", value=f"https://www.roblox.com/game-pass/23106709/6-mil-dhc")
        await interaction.response.send_message(embed=embed)
    elif amount.value == 7:
        embed = discord.Embed(color=0x2F3136)
        embed.set_author(name=interaction.user, icon_url=interaction.user.avatar)
        embed.add_field(name="**gamepass // dahood**", value=f"https://www.roblox.com/game-pass/23106710/7-mil-dhc")
        await interaction.response.send_message(embed=embed)
    elif amount.value == 8:
        embed = discord.Embed(color=0x2F3136)
        embed.set_author(name=interaction.user, icon_url=interaction.user.avatar)
        embed.add_field(name="**gamepass // dahood**", value=f"https://www.roblox.com/game-pass/23106717/8-mil-dhc")
        await interaction.response.send_message(embed=embed)
    elif amount.value == 9:
        embed = discord.Embed(color=0x2F3136)
        embed.set_author(name=interaction.user, icon_url=interaction.user.avatar)
        embed.add_field(name="**gamepass // dahood**", value=f"https://www.roblox.com/game-pass/23106730/9-mil-dhc")
        await interaction.response.send_message(embed=embed)
    elif amount.value == 10:
        embed = discord.Embed(color=0x2F3136)
        embed.set_author(name=interaction.user, icon_url=interaction.user.avatar)
        embed.add_field(name="**gamepass // dahood**", value=f"https://www.roblox.com/game-pass/23106731/10-mil-dhc")
        await interaction.response.send_message(embed=embed)    
    elif amount.value == 11:
        embed = discord.Embed(color=0x2F3136)
        embed.set_author(name=interaction.user, icon_url=interaction.user.avatar)
        embed.add_field(name="**gamepass // dahood**", value=f"https://www.roblox.com/game-pass/23106746/15-mil-dhc")
        await interaction.response.send_message(embed=embed)   
    elif amount.value == 12:
        embed = discord.Embed(color=0x2F3136)
        embed.set_author(name=interaction.user, icon_url=interaction.user.avatar)
        embed.add_field(name="**gamepass // dahood**", value=f"https://www.roblox.com/game-pass/23106737/20-mil-dhc")
        await interaction.response.send_message(embed=embed)   

@tree.command(name = "fastpass", description = "sends the type of fastpass you want to buy", guild=discord.Object(id=desiredRewrite.desiredRewriteV1_ServerID))
@app_commands.describe(type="type of fast pass to choose from")
@app_commands.choices(type=[
    discord.app_commands.Choice(name='one time fast pass [1]', value=1),
    discord.app_commands.Choice(name='one time fast pass [2]', value=2),
    discord.app_commands.Choice(name='permanent fast pass', value=3),
])
async def fastpass(interaction: discord.Interaction, type: discord.app_commands.Choice[int]):
    if type.value == 1:
        embed = discord.Embed(color=0x2F3136)
        embed.set_author(name=interaction.user, icon_url=interaction.user.avatar)
        embed.add_field(name="**gamepass // fast pass**", value=f"https://www.roblox.com/game-pass/23106633/one-time-fast-pass")
        await interaction.response.send_message(embed=embed)   
    elif type.value == 2:
        embed = discord.Embed(color=0x2F3136)
        embed.set_author(name=interaction.user, icon_url=interaction.user.avatar)
        embed.add_field(name="**gamepass // fast pass**", value=f"https://www.roblox.com/game-pass/23106530/one-time-fast-pass-2")
        await interaction.response.send_message(embed=embed)   
    elif type.value == 3:
        embed = discord.Embed(color=0x2F3136)
        embed.set_author(name=interaction.user, icon_url=interaction.user.avatar)
        embed.add_field(name="**gamepass // fast pass**", value=f"https://www.roblox.com/game-pass/23106537/perma-fast-pass")
        await interaction.response.send_message(embed=embed)   

@tree.command(name = "sub", description = "sends the type of subscription you want to buy", guild=discord.Object(id=desiredRewrite.desiredRewriteV1_ServerID))
@app_commands.describe(type="type of subscription to choose from")
@app_commands.choices(type=[
    discord.app_commands.Choice(name='bronze', value=1),
    discord.app_commands.Choice(name='gold', value=2),
    discord.app_commands.Choice(name='platinum', value=3),
    discord.app_commands.Choice(name='diamond', value=4),
])
async def sub(interaction: discord.Interaction, type: discord.app_commands.Choice[int]):
    if type.value == 1:
        embed = discord.Embed(color=0x2F3136)
        embed.set_author(name=interaction.user, icon_url=interaction.user.avatar)
        embed.add_field(name="**gamepass // subscription**", value=f"https://www.roblox.com/game-pass/85614118/bronze")
        await interaction.response.send_message(embed=embed)  
    elif type.value == 2:
        embed = discord.Embed(color=0x2F3136)
        embed.set_author(name=interaction.user, icon_url=interaction.user.avatar)
        embed.add_field(name="**gamepass // subscription**", value=f"https://www.roblox.com/game-pass/85614187/gold")
        await interaction.response.send_message(embed=embed)  
    elif type.value == 3:
        embed = discord.Embed(color=0x2F3136)
        embed.set_author(name=interaction.user, icon_url=interaction.user.avatar)
        embed.add_field(name="**gamepass // subscription**", value=f"https://www.roblox.com/game-pass/85614234/platinum")
        await interaction.response.send_message(embed=embed)  
    elif type.value == 4:
        embed = discord.Embed(color=0x2F3136)
        embed.set_author(name=interaction.user, icon_url=interaction.user.avatar)
        embed.add_field(name="**gamepass // subscription**", value=f"https://www.roblox.com/game-pass/85614285/diamond")
        await interaction.response.send_message(embed=embed)  

@tree.command(name = "pendannc", description = "sends a message into the annoucement channel for predropped cash", guild=discord.Object(id=desiredRewrite.desiredRewriteV1_ServerID))
async def pendannc(interaction: discord.Interaction, amount: str):
    bot.role = interaction.guild.get_role(desiredRewrite.desiredRewriteV1_RoleRequiredID)
    if bot.role not in interaction.user.roles:
        await interaction.response.send_message("**`failed`** `//` **`you do not have permission to run this command!`**")
    else:
        embed = discord.Embed(color=0x2F3136)
        embed.set_author(name=interaction.user, icon_url=interaction.user.avatar)
        embed.add_field(name="**pendannc // predropped!**", value=f"{interaction.user} has dropped {amount}! ping them in your ticket to claim")
        await interaction.response.send_message("<@&1051069786085396520>", embed=embed)  

@tree.command(name = "csub", description="checks your current subscription", guild=discord.Object(id=desiredRewrite.desiredRewriteV1_ServerID))
async def csub(interaction: discord.Interaction):
    casual = discord.utils.get(interaction.guild.roles, id=1068817202934980628)
    bronze = discord.utils.get(interaction.guild.roles, id=1068817214486097920)
    gold = discord.utils.get(interaction.guild.roles, id=1068817221830311966)
    platinum = discord.utils.get(interaction.guild.roles, id=1068817240272674856)
    diamond = discord.utils.get(interaction.guild.roles, id=1068817244160802876)

    if casual in interaction.user.roles:
        embed = discord.Embed(color=0x2F3136)
        embed.set_author(name=interaction.user, icon_url=interaction.user.avatar)
        embed.add_field(name="**subscription**", value="current subscription - `casual`")
        await interaction.response.send_message(embed=embed)
    if bronze in interaction.user.roles:
        embed1 = discord.Embed(color=0x2F3136)
        embed1.set_author(name=interaction.user, icon_url=interaction.user.avatar)
        embed1.add_field(name="**subscription**", value="current subscription - `bronze`")
        await interaction.response.send_message(embed=embed1)
    if gold in interaction.user.roles:
        embed2 = discord.Embed(color=0x2F3136)
        embed2.set_author(name=interaction.user, icon_url=interaction.user.avatar)
        embed2.add_field(name="**subscription**", value="current subscription - `gold`")
        await interaction.response.send_message(embed=embed2)
    if platinum in interaction.user.roles:
        embed3 = discord.Embed(color=0x2F3136)
        embed3.set_author(name=interaction.user, icon_url=interaction.user.avatar)
        embed3.add_field(name="**subscription**", value="current subscription - `platinum`")
        await interaction.response.send_message(embed=embed3) 
    if diamond in interaction.user.roles:
        embed4 = discord.Embed(color=0x2F3136)
        embed4.set_author(name=interaction.user, icon_url=interaction.user.avatar)
        embed4.add_field(name="**subscription**", value="current subscription - `diamond`")
        await interaction.response.send_message(embed=embed4)

@tree.command(name = "wl", description="adds a member a subscription", guild=discord.Object(id=desiredRewrite.desiredRewriteV1_ServerID))
@app_commands.describe(type="type of subscription to choose from")
@app_commands.choices(type=[
    discord.app_commands.Choice(name='casual', value=1),
    discord.app_commands.Choice(name='bronze', value=2),
    discord.app_commands.Choice(name='gold', value=3),
    discord.app_commands.Choice(name='platinum', value=4),
    discord.app_commands.Choice(name='diamond', value=5),
])
async def wl(interaction: discord.Interaction, type: discord.app_commands.Choice[int]):
    bot.role = interaction.guild.get_role(desiredRewrite.desiredRewriteV1_RoleRequiredID)
    if bot.role not in interaction.user.roles:
        await interaction.response.send_message("**`failed`** `//` **`you do not have permission to run this command!`**")
    else: 
        casual = interaction.guild.get_role(972493889573388298)
        bronze = interaction.guild.get_role(972493900214321244)
        gold = interaction.guild.get_role(972493913254428724)
        platinum = interaction.guild.get_role(972493916714725437)
        diamond = interaction.guild.get_role(972493919763980349)
        if type.value == 1:
            await interaction.user.add_roles(casual) 
            embed = discord.Embed(color=0x2F3136)
            embed.set_author(name=interaction.user, icon_url=interaction.user.avatar)
            embed.add_field(name="**upgraded!**", value=f"{interaction.user.name}'s subscription upgraded to // `casual`")
            await interaction.response.send_message(embed=embed)  
        elif type.value == 2:
            await interaction.user.add_roles(bronze) 
            embed = discord.Embed(color=0x2F3136)
            embed.set_author(name=interaction.user, icon_url=interaction.user.avatar)
            embed.add_field(name="**upgraded!**", value=f"{interaction.user.name}'s subscription upgraded to // `bronze`")
            await interaction.response.send_message(embed=embed)  
        elif type.value == 3:
            await interaction.user.add_roles(gold) 
            embed = discord.Embed(color=0x2F3136)
            embed.set_author(name=interaction.user, icon_url=interaction.user.avatar)
            embed.add_field(name="**upgraded!**", value=f"{interaction.user.name}'s subscription upgraded to // `gold`")
            await interaction.response.send_message(embed=embed)  
        elif type.value == 4:
            await interaction.user.add_roles(platinum) 
            embed = discord.Embed(color=0x2F3136)
            embed.set_author(name=interaction.user, icon_url=interaction.user.avatar)
            embed.add_field(name="**upgraded!**", value=f"{interaction.user.name}'s subscription upgraded to // `platinum`")
            await interaction.response.send_message(embed=embed)  
        elif type.value == 5:
            await interaction.user.add_roles(diamond) 
            embed = discord.Embed(color=0x2F3136)
            embed.set_author(name=interaction.user, icon_url=interaction.user.avatar)
            embed.add_field(name="**upgraded!**", value=f"{interaction.user.name}'s subscription upgraded to // `diamond`")
            await interaction.response.send_message(embed=embed)  

# -----------------------------------------------

@bot.event 
async def on_ready():
    await tree.sync(guild=discord.Object(id=desiredRewrite.desiredRewriteV1_ServerID))
    print('{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()) + desiredRewrite.desiredRewriteV1_Text_BoldFont + desiredRewrite.desiredRewriteV1_Color_Blue + " INFO     " + desiredRewrite.desiredRewriteV1_Text_Color_End + desiredRewrite.desiredRewriteV1_Color_Purple + "discord.gateway" + desiredRewrite.desiredRewriteV1_Text_Color_End + f" logged in {bot.user} [{bot.user.id}].")

bot.run(desiredRewrite.desiredRewriteV1_BotToken)
