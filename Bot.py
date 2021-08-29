import discord
from dotenv import load_dotenv
import os
load_dotenv('.env')

client = discord.Client()
RainbowSixQ = []

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$join'):
        await message.channel.send('Hello!'+ " " + str(message.author.display_name) + " " + "you have joined 'InsertUsersnameHere' RainbowSixQ you are {}")
        RainbowSixQ.append(str(message.author.display_name))
        print(RainbowSixQ)
    
    if message.content.startswith('$list'):
        await message.channel.send(RainbowSixQ)
        
    if message.content.startswith('$help'):
        await message.channel.send("This is the help menu for this bot.")
        
        
    if message.content.startswith('$delete'):
        await message.channel.send("Removing Next player from Q. {0.RainbowSixQ}".format(RainbowSixQ[1:]))

    
        

client.run(os.getenv('TOKEN'))
