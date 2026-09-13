import pyttsx3
import speech_recognition as sr


def speak(text):
    print(f"Assistant is trying to say: {text}")  # Debugging line
    try:
        # We initialize the engine INSIDE the function so it works with the thread
        speaker = pyttsx3.init('sapi5')
        voices = speaker.getProperty('voices')
        speaker.setProperty('voice', voices[0].id)
        speaker.setProperty('rate', 180)

        speaker.say(text)
        speaker.runAndWait()

        # We stop it properly so the next call can start fresh
        speaker.stop()
        del speaker  # Clean up the engine instance
    except Exception as e:
        print(f"Speech Engine Error: {e}")


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=8)
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}")
            return query.lower()
        except Exception:
            return "none"