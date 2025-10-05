import speech_recognition as sr
import webbrowser
import random
import multiprocessing
import pyttsx3
import re
import requests
import os
from musiclib import music
from dotenv import load_dotenv
from groq import Groq



def speak_process(text):
    # Text-to-speech engine (runs in a separate process)
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate',190)
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


def open_song(command):
    cmd = normalize(command)
    for key, url in music.items():
        if key in cmd:
            webbrowser.open(url)
            speak(f"Playing {key.title()} on YouTube")
            return True
    return False


def get_news():
    try:
        news_api = os.getenv("NEWS_API_KEY")
        news_url = f"https://newsapi.org/v2/everything?q=India&language=en&sortBy=publishedAt&apiKey={news_api}"

        response = requests.get(news_url)
        data = response.json()

        articles = data.get("articles", [])

        if not articles:
            speak("Sorry, I couldn’t find any fresh news at the moment.")
            return

        top_articles = articles[:3]  # read top 3
        speak("Here are the top headlines.")

        for i, article in enumerate(top_articles, 1):
            title = article.get("title", "No title available")
            print(f"{i}. {title}")  # For debugging
            speak(f"{i}. {title}")

    except Exception as err:
        speak("There was a problem fetching the news.")
        print("Error:", err)


# GROQ AI
load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")  
client = Groq(api_key = API_KEY)


def ask_luna(prompt):
    """Send user input to Groq AI and return the response"""
    try:
        chat_completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile", 
            messages=[
                {"role": "system", "content": "You are a virtual assistant named Luna."},
                {"role": "user", "content": prompt}
            ]
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        print("Error calling AI:", e)
        return "Sorry, I couldn't get an answer right now."



# Command to URL mapping 
commands = {
    "open google": "https://google.com",
    "open youtube": "https://youtube.com",
    "open linkedin": "https://linkedin.com",
    "open github": "https://github.com"
}

def process_command(c):
    cmd = normalize(c)
    
    # Play song on youtube
    if "play" in cmd:
        if open_song(cmd):
            return          # song found and opened
        else:
            speak("Sorry, I couldn't find that song.")
            return

    # News
    if "news" in cmd:
        speak("Fetching latest headlines for you")
        get_news()
        return
    
    # open websites
    for key, url in commands.items():
        if normalize(key) in cmd:
            site_name = key.split()[1].capitalize()
            speak(f"Opening {site_name}")
            webbrowser.open(url)
            return

    # anything else feed to groq ai
    response = ask_luna(c)
    speak(response)



def main():
    recognizer = sr.Recognizer()
    speak("Initializing Luna")

    while True:
        try:
            # Listen for wake word
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source,duration = 0.1)
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
                    audio = recognizer.listen(source, timeout=10, phrase_time_limit=15)
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
