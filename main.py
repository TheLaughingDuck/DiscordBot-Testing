import discord
from dotenv import load_dotenv
import os

#Load the .env file
load_dotenv()

#TEST PRINTS
print("I am running the script.")

#Create an instance of a client
#Intents specification required apparently
intents = discord.Intents.all()
client = discord.Client(intents=intents)

#Specify a channel
#channel = client.get_channel(997984431883173958)

@client.event
async def on_ready():
    print('I have logged in as {0.user}'.format(client))

    channel = client.get_channel(997984431883173958)
    await channel.send("I have been deployed!")




@client.event
async def on_message(message):
  #print("------------------")
  #print("Message event started")

  if(message.author == client.user):
    print("Message by self detected")
    return

  if message.content == '$hello':
    channel = message.channel
    await channel.send('Hello to you!')
    print("Hello to you!")

  if message.content == "$books":
    await message.channel.send("I like books")
    print("I like books")
  
  print("Message event code finished")


client.run(os.environ["KEY3"], bot=True)