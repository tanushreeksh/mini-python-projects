import speech_recognition as sr
import webbrowser
import random
import multiprocessing
import pyttsx3
import re


def speak_process(text):
    # Text-to-speech engine (runs in a separate process)
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()


def speak(text):
    # Wrapper for TTS to prevent microphone blocking
    print(f"Luna says: {text}")
    p = multiprocessing.Process(target=speak_process, args=(text,))
    p.start()
    p.join()  # wait until speaking is done


def normalize(text):
    """Lowercase, remove punctuation, and extra spaces."""
    text = text.lower()
    text = re.sub(r"[^a-z ]", "", text)     # remove anything that's not a letter or space
    text = " ".join(text.split())           # remove extra spaces
    return text

# Command to URL mapping 
commands = {
    "open google": "https://google.com",
    "open youtube": "https://youtube.com",
    "open linkedin": "https://linkedin.com",
    "open github": "https://github.com"
}

def process_command(command):
    cmd = normalize(command)
    for key, url in commands.items():
        if normalize(key) in cmd:           # normalize both sides
            site_name = key.split()[1].capitalize()
            speak(f"Opening {site_name}")
            webbrowser.open(url)
            return
    speak("Sorry, I don't know that command.")




def main():
    recognizer = sr.Recognizer()
    speak("Initializing Luna")


    while True:
        try:
            # Listen for wake word
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source, duration=1)
                print("Ready for wake word...")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=4)

            try:
                word = recognizer.recognize_google(audio)
                print(f"Heard: {word}")
            except Exception as err:
                print(err)
                continue


            # Wake word detected
            if "luna" in word.lower():
                speak(random.choice(["Yes?", "I'm listening."]))

                # Listen for command
                with sr.Microphone() as source:
                    print("Luna active, listening for command...")
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=6)
                    try:
                        command = recognizer.recognize_google(audio)
                        print(f"Command: {command}")
                        process_command(command)
                    except Exception as err:
                        speak(f"Sorry, I didn't understand that {err}")

        except sr.WaitTimeoutError:
            continue  # timeout, keep listening
        except Exception as e:
            print(f"Error occurred: {e}")


if __name__ == "__main__":
    main()
