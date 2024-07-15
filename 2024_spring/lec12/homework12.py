from gtts import gTTS

def synthesize(text, lang, filename):
    tts = gTTS(text=text, lang=lang)
    
    tts.save(filename)