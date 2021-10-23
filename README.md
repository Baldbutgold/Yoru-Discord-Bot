# Simple Discord Bot for Yoru's Server

This bot is a simple bot with some simple features,  
You can invite the bot from there.

### Features

***extract*** allow you to extract XYZ cords from a minecraft F3 screenshot  
***$type*** It types that simple xD  
***$help*** A function that displays all commands that are available   
***$say*** joins the person who sent the message Vc and says whatever is follwed by the $say </br>
***$start*** & ***$stop*** starts and stops the minecraft server </br>
***$world*** Send a link for the world download of minecraft </br>


### Upcoming Features

***$google*** Googles something either returns a brief on the topic or a list of links </br>
***$listen*** Listens to what you are saying in voice chat and types it as text or say it back with a twist like a monster voice
***xo*** Be Ready to play X & O tictactoe

#### Why I'm doing this?

It all started when I noticied that my friend group while playing on our minecraft server was taking a lot of screenshots to save the XYZ, and to remember the location, I thought to myself if there was just something that could extract the XYZ render it as a text maybe also save it to a location name, so the idea settled in my mind for a day </br>
Started working on it the next day,
Then the issue of making it something my friends can use came up so I decided to make it a discord bot. 

#### Difficulties and How I overcame them

##### Extracting the XYZ

This was one of the biggest **problems** it took me more than 3 hours and 2 days _as in 1.5hour in a day xD_ to figure this out, now the initial idea was simple to crop the image and extract the cords as a screenshot then figure the rest out, suddenly i was faced by the fact the there is different screen sizes, and you can crop all of them the same size, I dumped the idea, and moved it to the next idea which was where i started getting stuck </br>

Manuplating the colors, I had no idea what i was doing so i learned step by step, PIL, cv2, numpy, still don't know shit about numpy xD </br>

I got stuck so i googled a tutorial I found something, a person using [**Binarization**](https://felixniklas.com/imageprocessing/binarization) by the way Binarization is the process of converting a pixel image to a binary image.
</br>

This opened a new whole possiblities but still was to difficult to implement _maybe in the future I can make a simple website that uses Binaraztion_.</br>

And for this to even work I need to use an algorithim called Adaptive threshold, simple for you to binarizate an image you need to set a threshold if a pixel is above a color set it to this color if it is less then set it to this other color, and the issue with this is that there is some many colors in those minecraft screenshot it is impossible for you to set a threshold and Hope that it i will make the whole image white and black leaving the text clear for you to analyze.</br>

###### Going back to the start

Simply after asking a friend for help he was like just crop it simple, and then it hit why don't i crop using the width and height of the image BOOM it worked 90% succes _based on my 10 differnet screenshots_

###### It is all coming along

The time i wasted figuring out binarization, Tought me a how to crop image how to change color blah blah, I also Learned **OCR** which stands for **Optical Charcter Recognition** from an image to a text using [pytesseract](https://pypi.org/project/pytesseract/) the process installation was a bit hard NGL, you need to install them as a program apt install tesseract and then in python as well, then using something called LANG helps the program to identify based on a font or a language, that I jsut grabbed from the internet techincally you need to train the algorithm **machine learning** which i don't know nothing about xD.</br>
So yea it alll worked at the end _burst of dopamine_ xD.

#### Making it to a Discord bot

I had a lot of trail and error with this, major problem was grabbing the image and saving it _pain in my ass_, I readed the docs, stack overflow no hope until i decided to just watch a youtube video about a guy bot that saves the whole images in a channel, Found out his github repo and then I found out this command built in discord :)</br>

await message.attachments[0].save('nameyouwanttosave') </br>
REALLY DISCORD xD that was a pain tbh,
But I felt so stupid and dumb,</br>

I guess those were all the difficulties worth mentioning

### Time to Build it

It took me around 10 hours I guess I only documanted 5 hours xD,
I just got so deep it tbh

### Spoiler

They never used it HHHHHHHHHHHHHHHHHHHHHHHHHHHHH
