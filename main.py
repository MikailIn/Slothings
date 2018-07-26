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
    print(
        "  _____ _       _   _     \n / ____| |     | | | |    \n| (___ | | ___ | |_| |__  \n \___ \| |/ _ \| __| '"
        "_ \ \n ____) | | (_) | |_| | | |\n|_____/|_|\___/ \__|_| |_|")
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
    message = ctx.message.content.lower()
    if message == "?help":
        em = discord.Embed(title="Sloth commands", colour=0xF4B042)
        em.add_field(name="Moderation", value="Some moderation commands for the mods.", inline=False)
        em.add_field(name="Miscellaneous", value="Misc commands to have fun with!", inline=False)
        em.add_field(name="Information", value="Get information about the bot here!", inline=False)
        em.set_footer(text="Type ?help <mod/misc/...> to see the list of commands")
        await bot.say(embed=em)
    if message == "?help moderation" or message == "?help mod":
        em = discord.Embed(title="Moderation commands", colour=0xF4B042)
        em.add_field(name="?ban", value="ban the specified user", inline=True)
        em.add_field(name="\u200b", value="requires ban members permission", inline=True)
        em.add_field(name="\u200b", value="\u200b", inline=True)
        em.add_field(name="?kick", value="kick the specified user", inline=True)
        em.add_field(name="\u200b", value="requires kick members permission", inline=True)
        em.add_field(name="\u200b", value="\u200b", inline=True)
        await bot.say(embed=em)
    if message == "?help miscellaneous" or message == "?help misc":
        em = discord.Embed(title="Miscellaneous commands", colour=0xF4B042)
        em.add_field(name="?ping", value="returns pong!", inline=True)
        em.add_field(name="\u200b", value="\u200b", inline=True)
        em.add_field(name="\u200b", value="\u200b", inline=True)
        em.add_field(name="?say", value="repeats after you", inline=True)
        em.add_field(name="\u200b", value="\u200b", inline=True)
        em.add_field(name="\u200b", value="\u200b", inline=True)
        em.add_field(name="?sloth", value="posts an image of a cute sloth", inline=True)
        em.add_field(name="\u200b", value="\u200b", inline=True)
        em.add_field(name="\u200b", value="\u200b", inline=True)
        await bot.say(embed=em)
    if message == "?help information" or message == "?help info":
        em = discord.Embed(title="Miscellaneous commands", colour=0xF4B042)
        em.add_field(name="?help", value="opens help", inline=True)
        em.add_field(name="\u200b", value="\u200b", inline=True)
        em.add_field(name="\u200b", value="\u200b", inline=True)
        em.add_field(name="?invite", value="gives the bot invite link", inline=True)
        em.add_field(name="\u200b", value="\u200b", inline=True)
        em.add_field(name="\u200b", value="\u200b", inline=True)
        em.add_field(name="?suggest", value="suggest something to the bot owner", inline=True)
        em.add_field(name="\u200b", value="\u200b", inline=True)
        em.add_field(name="\u200b", value="\u200b", inline=True)
        em.add_field(name="?git", value="posts the github repository of the bot", inline=True)
        em.add_field(name="\u200b", value="\u200b", inline=True)
        em.add_field(name="\u200b", value="\u200b", inline=True)
        await bot.say(embed=em)


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


@bot.command()
async def git():
    await bot.say("**The github repository of the bot:**\nhttps://www.github.com/MrVestacus/Sloth")


bot.run(token)
