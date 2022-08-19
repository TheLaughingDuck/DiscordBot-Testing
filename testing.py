import discord
import os
from dotenv import load_dotenv


load_dotenv()

#Required apparently
intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('I have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if(message.author == client.user):
        return
    
    if(message.content == "$hello"):
        await message.channel.send("Hello to you!")
    
    if(message.content == ""):
        await message.channel.send('That was an empty message')
    
    

client.run(os.environ["KEY3"])
