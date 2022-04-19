import discord
from discord.ext import commands

client = discord.Client()
bot = commands.Bot(command_prefix='$')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$awok'):
        await message.channel.send('awokawokawokawok')

    if message.content.startswith('$ya'):
        await message.channel.send('drian si paling ganteng')
    if message.content.startswith('$re'):
        await message.channel.send('rizka si paling jelek'+ '1')

        
    if message.content.startswith('$help'):
        await message.channel.send("```Perintahnya $awok, $re, $ya```")

    

@client.event
async def mulai(message):
    await message.clannel.send(message)  
        


client.run('OTMxNDQxMjA1MTMxMjI3MTU2.YeEeOA.P-a0bwr1EI6WgYc2Rk9PeHYxfR0')
