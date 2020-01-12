import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')
#When the bot is connected will print status

@bot.command()
async def poll(ctx, arg):
    if arg is None:
        return
    else:
        msg = await ctx.send(arg)
        await msg.add_reaction('1️⃣')
        await msg.add_reaction('2️⃣')


#Do not put api key in when pushing to repo
bot.run('')
