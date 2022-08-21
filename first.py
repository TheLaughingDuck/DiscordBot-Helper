import discord
from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

# Test print
print("------------------------")
print("The script is being run.")
print("Hello world.")
print("------------------------")


# Create an instance of a CLIENT
intents = discord.Intents.all()
client = discord.Client(intents=intents)


# EVENT on START
@client.event
async def on_ready():
    print("I have now logged in as {0.user}".format(client))

    channel = client.get_channel(997984431883173958)
    await channel.send("I have been awoken!")



# RUN the CLIENT
client.run(os.environ["KEY1"], bot=True)