from decouple import config
import os 
import discord
import image2text

client = discord.Client()


@client.event
async def on_ready():
    print("I am good to go")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
#type back prefix=$type
    elif message.content.startswith("$type"):
        msg = message.content[5:]
        await message.delete()
        await message.channel.send(msg)


#cords extractor prefix=extract
    if message.content.startswith("extract"):
#        await message.channel.send(message.attachments[0])
        await message.attachments[0].save('image.png')
        img2txt = image2text.image2text()
        #a module that crops the image into the xyz pos, and extract text, returns only text
        await message.channel.send(img2txt, file=discord.File('img.png'))
    if message.content.startswith("$help"):
        #simple help function
        await message.channel.send("""
        $type I will type something back to you
extract I will extract cords from a minecraft F3 screenshot
Upcoming commands coming soon!
        """)

client.run(config('TOKEN'))
