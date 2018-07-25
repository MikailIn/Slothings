from discord.ext import commands


def check_if_owner():
    """checks if the user is the owner of the bot"""
    def predicate(ctx):
        if ctx.message.author.id == "183234193281646592":
            return True
        else:
            return False
    return commands.check(predicate)


def has_any_permission(**perms):
    def predicate(ctx):
        msg = ctx.message
        ch = msg.channel
        permissions = ch.permissions_for(msg.author)
        return any(getattr(permissions, perm, None) == value for perm, value in perms.items())
    return commands.check(predicate)