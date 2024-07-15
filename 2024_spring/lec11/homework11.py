import speech_recognition as sr

def transcribe_wavefile(filename, language='en'):
    recognizer = sr.Recognizer()
    
    with sr.AudioFile(filename) as source:
        audio_data = recognizer.record(source)
        
    try:
        text = recognizer.recognize_google(audio_data, language=language)
        return text
    except sr.UnknownValueError:
        return "Recognition could not understand audio"
    except sr.RequestError as e:
        return f"Error in API request: {str(e)}"