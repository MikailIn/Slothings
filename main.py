import discord
import asyncio
import random
from discord.ext import commands
from data.slothimages import sloth_images
from cogs.utils import checks

token = "NDY1NTAyMjYwOTQ5MDI0NzY4.DiOezw.I3JO-1DxmLPPizL_ke7dGGzrXaY"
bot = commands.Bot(command_prefix="?")
bot.remove_command("help")


@bot.event
async def on_ready():
    print("Logged in as")
    print(bot.user.name)
    print(bot.user.id)
    print("------")
    await bot.change_presence(game=discord.Game(name="with my dingdong"))


@bot.event
async def on_message(message):
    """reacts when someone types kys or kms"""
    if message.content.lower() == "kys" and not message.author.bot:
        await bot.send_message(message.channel, "no u")
    if message.content.lower() == "kms" and not message.author.bot:
        await bot.send_message(message.channel, "do it")
    await bot.process_commands(message)


@bot.command()
async def ping():
    """ping pong"""
    await bot.say(":ping_pong: Pong!")


@bot.command(no_pm=True)
async def say(*, message):
    """repeats something the user says"""
    await bot.say(message)


@bot.command(no_pm=True)
async def sloth():
    """gives a random image of a sloth"""
    output = random.sample(sloth_images, 1)
    em = discord.Embed(title="Have a sloth", colour=0xFF384B)
    em.set_image(url=output[0])
    await bot.say(embed=em)


@bot.command(pass_context=True)
@checks.check_if_owner()
async def addtodo(ctx, *, message):
    """add a to do task to your to do channel"""
    await bot.send_message(discord.Object(id="465513192865660956"), message)
    await bot.delete_message(ctx.message)
    await bot.say("Yes master, I added it to your to do list :eggplant:")


@bot.command(pass_context=True)
async def suggest(ctx, *, message):
    """command to suggest something"""
    author = ctx.message.author
    output = "{} - {}".format(message, author)
    await bot.send_message(discord.Object(id="465513216034734080"), output)
    await bot.say("Yes sir, I heard your calls and will relay it to my master :eggplant:")


@bot.command(pass_context=True)
async def help(ctx):
    """help command"""
    p = ctx.prefix
    em_owner = discord.Embed(colour=0xF4B042)
    em_owner.set_author(name="Bot owner commands")
    em_owner.add_field(name="{}addtodo".format(p), value="Adds something to the todo channel", inline=False)
    await bot.say(embed=em_owner)
    em_user = discord.Embed(colour=0xF4B042)
    em_user.set_author(name="User commands")
    em_user.add_field(name="{}ping".format(p), value="Returns Pong", inline=False)
    em_user.add_field(name="{}say".format(p), value="Repeats after you", inline=False)
    em_user.add_field(name="{}sloth".format(p), value="Returns an image or a gif of a sloth", inline=False)
    em_user.add_field(name="{}suggest something".format(p), value="Suggests something", inline=False)
    em_user.add_field(name="{}invite".format(p), value="Returns the invite link of the bot", inline=False)
    em_user.add_field(name="{}kick @someone reason".format(p), value="Kicks someone", inline=False)
    em_user.add_field(name="{}ban @someone reason".format(p), value="Bans someone", inline=False)
    await bot.say(embed=em_user)


@bot.command()
async def invite():
    """gives the bot invite link"""
    url = "https://discordapp.com/api/oauth2/authorize?client_id=462878456598888449&permissions=469888118&scope=bot"
    await bot.say("**My invite link:**\n{}".format(url))


@bot.command(pass_context=True)
@commands.has_permissions(kick_members=True)
@commands.bot_has_permissions(kick_members=True)
async def kick(ctx, username: discord.User):
    """kicks someone"""
    server = ctx.message.server
    message = ctx.message.content.split()
    reason = " ".join(message[2:])
    if reason == "":
        await bot.send_message(username, "You were kicked from **{}**.".format(server))
    else:
        await bot.say(reason)
        await bot.send_message(username, "You were kicked from **{}**. Reason:\n*{}*".format(server, reason))
    await bot.kick(username)
    await bot.say("{} got kicked from the server. Bye-bye :wave:".format(username))


@bot.command(pass_context=True)
@commands.has_permissions(ban_members=True)
@commands.bot_has_permissions(ban_members=True)
async def ban(ctx, username: discord.User):
    """bans someone"""
    server = ctx.message.server
    message = ctx.message.content.split()
    reason = " ".join(message[2:])
    if reason == "":
        await bot.send_message(username, "You were banned from **{}**.".format(server))
    else:
        await bot.say(reason)
        await bot.send_message(username, "You were banned from **{}**. Reason:\n*{}*".format(server, reason))
    await bot.ban(username, delete_message_days=0)
    await bot.say("{} got banned from the server. Poor soul, they did not deserve this (╯°□°）╯︵ ┻━┻".format(username))


bot.run(token)
