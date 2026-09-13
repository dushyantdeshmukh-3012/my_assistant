import datetime
import wikipedia


def get_time():
    t = datetime.datetime.now().strftime("%I:%M %p")
    screen_text = f"\n\n\n          CURRENT TIME\n\n               {t}"
    voice_text = f"The time is {t}"
    return screen_text, voice_text


def get_date():
    d = datetime.datetime.now().strftime("%A, %B %d, %Y")
    screen_text = f"\n\n\n          TODAY'S DATE\n\n    {d}"
    voice_text = f"Today is {d}"
    return screen_text, voice_text


def search_wikipedia(query):
    try:
        # FIX: Added auto_suggest=False to prevent the space/suggestion bug from crashing the script
        summary = wikipedia.summary(query, sentences=3, auto_suggest=False)

        screen_text = f"WIKIPEDIA SEARCH: {query.upper()}\n\n{summary}"
        voice_text = summary
        return screen_text, voice_text

    except wikipedia.exceptions.DisambiguationError as e:
        # Triggered when a word has multiple meanings
        options = ", ".join(e.options[:3])  # grab first 3 alternatives
        fail_msg = f"Too ambiguous. Did you mean: {options}?"
        return fail_msg, "Multiple topics matched. Please be more specific."

    except wikipedia.exceptions.PageError:
        # Triggered when the page absolutely does not exist
        return f"No results found for '{query}'.", f"I could not find any pages matching {query}."

    except Exception as e:
        # Fallback error catcher
        return f"Connection Error: {str(e)}", "I encountered an error connecting to Wikipedia."