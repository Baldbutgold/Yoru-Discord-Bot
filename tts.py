from gtts import gTTS

def ttsmp3(text):
    tts = gTTS(text)
    tts.save('say.mp3')
