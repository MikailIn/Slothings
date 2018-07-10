import discord
import asyncio
import random
import os
from discord.ext import commands
from slothimages import sloth_images

token = "NDY1NTAyMjYwOTQ5MDI0NzY4.DiOezw.I3JO-1DxmLPPizL_ke7dGGzrXaY"
bot = commands.Bot(command_prefix="?")
bot.remove_command("help")


def check_if_owner():
    """checks if the user is the owner of the bot"""
    def predicate(ctx):
        if ctx.message.author.id == "183234193281646592":
            return True
        else:
            return False
    return commands.check(predicate)


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
@check_if_owner()
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
    p = ctx.prefix
    em_owner = discord.Embed(colour=0xF4B042)
    em_owner.set_author(name="Bot owner commands")
    em_owner.add_field(name="{}addtodo something".format(p), value="Adds something to your to do channel", inline=False)
    await bot.say(embed=em_owner)
    em_user = discord.Embed(colour=0xF4B042)
    em_user.set_author(name="User commands")
    em_user.add_field(name="{}ping".format(p), value="Returns Pong", inline=False)
    em_user.add_field(name="{}say something".format(p), value="Returns something", inline=False)
    em_user.add_field(name="{}sloth".format(p), value="Returns an image or a gif of a sloth", inline=False)
    em_user.add_field(name="{}suggest something".format(p), value="Adds something to your suggestion channel", inline=False)
    await bot.say(embed=em_user)


bot.run(token)
