````markdown
# Luna – Voice Assistant

Luna is a simple Python-based voice assistant that listens for a wake word and executes basic commands like opening websites.  
It uses **SpeechRecognition**, **pyttsx3**, and **multiprocessing** for smooth voice interaction.


## Features
- Wake word detection ("Luna")
- Voice feedback using text-to-speech
- Open common websites (Google, YouTube, LinkedIn, Github, Spotify)
- Runs commands in a separate process to avoid microphone blocking
- Easy to extend with more commands


## Requirements
- Python 3.8+
- Microphone access

### Install dependencies:
```bash
pip install SpeechRecognition pyttsx3
```


## Usage
Run the assistant:

```bash
python luna.py
```

Workflow:
1. Say **"Luna"** as the wake word.
2. After activation, speak a command (e.g., *"open Google"*).
3. Luna will respond and take action.

```
