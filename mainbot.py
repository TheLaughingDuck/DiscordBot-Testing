import discord
import os


#Create an instance of a client
client = discord.Client()

@client.event
async def on_ready():
    print('I have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if(message.author == client.user):
        return
    
    if(message.content == '$hello'):
        await message.channel.send('Hello world!')


client.run(os.environ['key3'])

