import discord
import os


client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    gmae = discord.Game("SIRI")
    await client.change_preasencd(status=discord.Status.online, activity=gam)

@client.event
async def on_message(message):
    if message.content.startswith("안녕"):
        await message.channel.send("반가워용")
    if message.content.startswith("잘가"):
        await message.channel.send("또만나요")


access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
