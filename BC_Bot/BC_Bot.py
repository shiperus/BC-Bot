import discord
from discord.ext import commands






#a = 20
#print(a)
bot = commands.Bot(command_prefix='ggz!', description='testing bot ggz')


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)

@bot.command()
async def hello():
    await bot.say("ggz mz")


@bot.command()
async def test(var):
    print(var)
    await bot.say("ggz mz")

@bot.event
async def on_message(message):
    if message.author.id == botId:
        return
    print(message)
    print(message.author.id)
    await bot.send_message(message.channel, 'RIP')

bot.run('Mzc4OTQzMzM0OTM0MzgwNTQ2.DOi2GQ.9y1XaiEXeQdH5JAD51CCe89KztI')

