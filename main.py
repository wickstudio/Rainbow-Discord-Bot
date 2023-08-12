import discord
import asyncio
import random
import config

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

TOKEN = config.TOKEN  # Set your bot token in config.py
SERVER_ID = config.SERVER_ID  # Set your server ID in config.py
ROLE_ID = config.ROLE_ID  # Set your role ID in config.py

client = discord.Client(intents=intents)

async def change_role_color():
    await client.wait_until_ready()
    guild = client.get_guild(SERVER_ID)
    role = guild.get_role(ROLE_ID)
    
    while not client.is_closed():
        new_color = discord.Colour(random.randint(0, 0xFFFFFF))
        await role.edit(colour=new_color)
        await asyncio.sleep(20)  # Update ever 20 seconds

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name} - {client.user.id}')
    client.loop.create_task(change_role_color())

client.run(TOKEN)

# Code by 约 - Wick
