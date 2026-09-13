import pywhatkit
import webbrowser

def play_on_youtube(topic):
    """Automatically opens YouTube and plays the top video for the topic"""
    pywhatkit.playonyt(topic)

def search_google(query):
    """Opens a browser tab and searches Google"""
    pywhatkit.search(query)

def open_website(url):
    """Opens any website (e.g., google.com, facebook.com)"""
    if not url.startswith("http"):
        url = "https://" + url
    webbrowser.open(url)