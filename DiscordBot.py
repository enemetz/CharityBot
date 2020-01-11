import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.content.startswith('!aminals'):
        await message.channel.send('This is a test')
#async def
client.run('')
