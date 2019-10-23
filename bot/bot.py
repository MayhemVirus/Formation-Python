# bot.py
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

client = discord.Client()
# bot = commands.Bot(command_prefix='$', description='Nope')

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    # await client.change_presence(game=discord.Game(name="Troll en cours..."))

# @bot.command()
# async def toutou(channel):
#     channel = client.get_channel(636523572965146636)
#     await channel.send(file=discord.File('toutou.jpeg'))
    
@client.event
async def on_message(message):
    
    if message.author == client.user:
        return
    if message.content.startswith('.vincent'):
        await message.channel.send(file=discord.File('toutou.jpeg'))
    elif message.content.startswith('.jeremy'):
        await message.channel.send(file=discord.File('capen.png'))
    elif message.content.startswith('.paulin'):
        await message.channel.send(file=discord.File('capen.png'))
    elif message.content.startswith('.akhmed'):
        await message.channel.send(file=discord.File('akhmed.jpg'))
    elif message.content == "Hello":
        await channel.send("World")
    
client.run(token)