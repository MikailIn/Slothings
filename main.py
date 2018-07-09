import discord
import asyncio
import random
import os
from discord.ext import commands
from discord.ext.commands import Bot

token = "NDY1NTAyMjYwOTQ5MDI0NzY4.DiOezw.I3JO-1DxmLPPizL_ke7dGGzrXaY"
bot = commands.Bot(command_prefix="?")

sloth_images = ["https://i.imgur.com/74ketp5.jpg", "https://i.imgur.com/27n3GOp.gif", "https://i.imgur.com/Y273oWN.gif",
                "https://i.imgur.com/ngEzEx3.jpg", "https://i.imgur.com/I1705Pl.jpg", "https://i.imgur.com/8NDtJIn.jpg",
                "https://i.imgur.com/EMgtKOm.png", "https://i.imgur.com/RraDXN9.jpg", "https://i.imgur.com/p8L1hIT.jpg",
                "https://i.imgur.com/JzIWQIM.gif", "https://i.imgur.com/l2KTb00.jpg", "https://i.imgur.com/puQuUs5.jpg",
                "https://i.imgur.com/YAcqg7w.jpg", "https://i.imgur.com/sBHrOkJ.gif", "https://i.imgur.com/sLtkdBr.jpg",
                "https://i.imgur.com/CDyCzXm.gif", "https://i.imgur.com/EnEP2yq.jpg", "https://i.imgur.com/Yepk0Ud.jpg",
                "https://i.imgur.com/xCfzNXO.jpg", "https://i.imgur.com/sOZZAir.gif", "https://i.imgur.com/LssIjF9.jpg",
                "https://i.imgur.com/wxEmLlC.jpg", "https://i.imgur.com/wfi5hJ6.jpg", "https://i.imgur.com/LS4ti6h.jpg",
                "https://i.imgur.com/Ykyij7u.jpg", "https://i.imgur.com/q6WOKq2.png", "https://i.imgur.com/ReRFgW4.jpg",
                "https://i.imgur.com/Xwc5Qg6.png", "https://i.imgur.com/otahtk4.gif", "https://i.imgur.com/zjW9r80.png",
                "https://i.imgur.com/Bct0Mdi.gif", "https://i.imgur.com/EdhlSbk.gif", "https://i.imgur.com/00ztlUs.gif",
                "https://i.imgur.com/y13e8nl.gif", "https://i.imgur.com/mF5H06x.gif", "https://i.imgur.com/jhgFhmX.gif",
                "https://i.imgur.com/fo4veCm.gif", "https://i.imgur.com/LVvVUrW.gif", "https://i.imgur.com/qtJPkBn.jpg",
                "https://i.imgur.com/A9AjH7f.jpg", "https://i.imgur.com/wCGMMH7.jpg", "https://i.imgur.com/kt8yN6j.jpg",
                "https://i.imgur.com/axcwJfK.jpg", "https://i.imgur.com/cVKBzvE.gif", "https://i.imgur.com/Jq6q8kc.jpg",
                "https://i.imgur.com/8OH7Dab.jpg", "https://i.imgur.com/M73UL6v.jpg", "https://i.imgur.com/hght8r4.jpg",
                "https://i.imgur.com/CFuGETz.jpg", "https://i.imgur.com/NG9WL3A.jpg", "https://i.imgur.com/NawCi3o.jpg",
                "https://i.imgur.com/9u6aHsL.jpg", "https://i.imgur.com/LsDP2qh.jpg", "https://i.imgur.com/abfB5Z7.jpg",
                "https://i.imgur.com/PPOUg39.jpg", "https://i.imgur.com/xvaS5e8.jpg", "https://i.imgur.com/W2YiMGU.jpg",
                "https://i.imgur.com/9WpsU4D.jpg", "https://i.imgur.com/rUvqb0s.jpg", "https://i.imgur.com/aeAHtoz.jpg",
                "https://i.imgur.com/QBFslbK.jpg", "https://i.imgur.com/8edeNwP.jpg", "https://i.imgur.com/WWqetVw.jpg",
                "https://i.imgur.com/VZRCpSg.jpg", "https://i.imgur.com/biVjC5X.jpg", "https://i.imgur.com/pVOvSZx.jpg",
                "https://i.imgur.com/77t9oi7.jpg", "https://i.imgur.com/CgsOKae.jpg", "https://i.imgur.com/GtTag4V.gif",
                "https://i.imgur.com/Gw4Lvbv.gif", "https://i.imgur.com/9Ukzhb7.gif"
                ]


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


bot.run(token)
