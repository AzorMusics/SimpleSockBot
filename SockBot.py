import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = 'BOT_TOKEN'
USER_ID = 000000000000000000 # This should be the Id of your Discord Account (the one you want it to respond to)

print("SockBot Single Script")

client = discord.Client()

@client.event
async def on_ready():
    print(
        
        f'{client.user} is connected'
    )



@client.event
async def on_message(message):
    lower = message.content.lower()

    if message.author.id == USER_ID:

        if message.content == "*kill":
            exit()
        else:
            await message.delete()
            await message.channel.send(message.content)
        
    
        
client.run(TOKEN)