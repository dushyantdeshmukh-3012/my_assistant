# An intelligent, voice-controlled desktop assistant built with Python

## 1) Features

The Smart AI Assistant is a hands-free desktop program that carries out daily computer tasks using simple voice commands. It listens to what you say and automatically searches Google, plays YouTube videos, reads Wikipedia answers aloud, sends WhatsApp messages, and tells you the current time or date. Everything runs on a clean, modern dark interface.

It provides the following features:

- Tells you the current time and date
- Fetches summaries from Wikipedia
- Searches Google for any topic requested by the user
- Plays YouTube videos
- Sends WhatsApp messages to people in your contact list

All the above tasks are performed using voice commands, so you don't need to type anything.

<br>

## 2) Prerequisites

To run the Smart AI Assistant, the following three basic prerequisites must be met:

### a) Windows Operating System

**Why:** The assistant relies on Windows' native SAPI5 text-to-speech system through `pyttsx3` for instant, offline voice responses.

**Requirement:** Windows 10 or Windows 11 (64-bit).

<br>

### b) Active Internet Connection

**Why:** Several core features depend on online services and web access.

**Requirement:** A stable internet connection is required for:

- Online speech recognition
- Searching Google and playing YouTube videos
- Fetching Wikipedia article summaries
- Sending WhatsApp messages
  
 <br>

### c) Working Audio Hardware

**Why:** The application is built around voice input and audio output.

**Requirement:**

- A working microphone (built-in laptop microphone or external headset)
- Working speakers or headphones to hear the assistant's responses (Most laptops have built-in speakers.)

<br>

## 3) Installation & Setup

Follow these steps to install and run the Smart AI Assistant on a Windows computer.

### **Step 1: Clone the Repository**
Make sure Git and Python (3.9–3.11 recommended) are installed on your computer. Open Command Prompt or a terminal and run the following commands:

**Clone the repository:**
```bash
git clone https://github.com/dushyantdeshmukh-3012/my_assistant.git
```

**Move into the `my_assistant` folder:**
```bash
cd my_assistant
```

> **Alternative:** You can also download the repository as a ZIP file from GitHub and extract it on your computer.

---

### **Step 2: Install Dependencies**
Install the required Python packages using the `requirements.txt` file:
```bash
python -m pip install -r requirements.txt
```

> **Troubleshooting `PyAudio`:** If `PyAudio` fails to build during installation, run the following commands instead:
> ```bash
> python -m pip install pipwin
> python -m pipwin install pyaudio
> ```

---

### **Step 3: Run the Assistant**
Launch the graphical user interface and start the voice assistant:
```bash
python app.py
```
