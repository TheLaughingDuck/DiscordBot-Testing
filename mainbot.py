import discord
from dotenv import load_dotenv
import os

#Load the .env file
load_dotenv()

#Create an instance of a client
client = discord.Client()

@client.event
async def on_ready():
    print('I have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):#
  if(message.author == client.user):
    return
  
  if(message.content == '$hello'):
    await message.channel.send("Hello world")
    print("Hello world!")

  if(message.content == '$books'):
    await message.channel.send("I like books")


client.run(os.environ['KEY3'])

