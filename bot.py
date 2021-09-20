from discord import FFmpegPCMAudio
from discord.utils import get
import tts
from decouple import config
import os 
import discord
import image2text

#logging to a file

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
#saying function joining vc and playing mp3 file

    elif message.content.startswith("$say"):
        say = message.content[4:]
        tts.ttsmp3(say)
        user = message.author
        channel= user.voice.channel
        if not channel:    
            await message.chnanel.send(f"{user} is not in a vc")
            return
        voice = get(client.voice_clients )
        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()
        source = FFmpegPCMAudio('say.mp3')
        player = voice.play(source)
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
        **$type** I will type something back to you
**extract** I will extract cords from a minecraft F3 screenshot
**$help** اسم على مسمى
**$say** I will say DUH...
Upcoming commands coming soon!
        """)

client.run(config('TOKEN'))
