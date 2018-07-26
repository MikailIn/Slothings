from discord.ext import commands


def check_if_owner():
    """checks if the user is the owner of the bot"""
    def predicate(ctx):
        if ctx.message.author.id == "183234193281646592":
            return True
        else:
            return False
    return commands.check(predicate)
