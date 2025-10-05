# **Luna** - Voice-Activated Assistant

**Luna** is a Python voice assistant that responds to commands, plays YouTube music, fetches news, opens websites, and answers general questions using Groq AI.  


### Features
- Wake-word activation ("Luna")
- Plays songs from YouTube
- Opens popular websites (Google, YouTube, LinkedIn, GitHub)
- Fetches latest news headlines
- Answers general questions using Groq AI


### Workflow:
- Say "Luna" as the wake word.
- After activation, speak a command, luna listens to your command and responds via speech.
- Commands can include:
    Web navigation: "open Google", "open YouTube", "open LinkedIn", "open GitHub".
    Music playback: "play [song name]" – opens the song on YouTube.
    News headlines: "news" – fetches the latest top headlines.
    General questions e.g: tell me about Edinburgh
- Repeat steps 1–4 for continuous interaction with Luna.


### Setup
1. Clone the repo and activate a Python virtual environment.

2.Add a .env file with:
- GROQ_API_KEY=<your-key>
- NEWS_API_KEY=<your-key>

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

