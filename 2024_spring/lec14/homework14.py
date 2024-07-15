import random
import speech_recognition as sr
from gtts import gTTS
import datetime

def what_time_is_it(lang, filename):
    now = datetime.datetime.now()
    time_string = now.strftime("%H:%M")
    tts = gTTS(text=f"The time is {time_string}", lang=lang)
    tts.save(filename)
    
def tell_me_a_joke(lang, audiofile):
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "What do you get if you cross a snowman and a vampire? Frostbite.",
        "Why did the scarecrow win an award? Because he was outstanding in his field."
    ]
    joke = random.choice(jokes)
    tts = gTTS(text=joke, lang=lang)
    tts.save(audiofile)

def what_day_is_it(lang, audiofile):
    now = datetime.datetime.now()
    day_string = now.strftime("%A, %B %d, %Y")
    tts = gTTS(text=f"Today is {day_string}", lang=lang)
    tts.save(audiofile)
    url = f"https://www.timeanddate.com/calendar/monthly.html?year={now.year}&month={now.month}"
    return url

def personal_assistant(lang, filename):
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    
    with mic as source:
        print("Listening...")
        audio = recognizer.listen(source)
        
    try:
        request = recognizer.recognize_google(audio)
        print(f"User said: {request}")
        
        if "time" in request.lower():
            what_time_is_it(lang, filename)
        elif "day" in request.lower():
            url = what_day_is_it(lang, filename)
            print(f"You can check the calendar here: {url}")
        elif "joke" in request.lower():
            tell_me_a_joke(lang, filename)
        else:
            tts = gTTS(text="I didn't understand that. Please ask for the time, the date, or a joke.", lang=lang)
            tts.save(filename)
    except sr.UnknownValueError:
        print("Sorry, I did not understand the audio.")
        tts = gTTS(text="Sorry, I did not understand the audio.", lang=lang)
        tts.save(filename)
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        tts = gTTS(text="Sorry, there was an error processing your request.", lang=lang)
        tts.save(filename)
