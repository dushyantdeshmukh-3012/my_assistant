import pywhatkit
import webbrowser
import time
import pyautogui

# --- YOUR CONTACT BOOK ---
contacts = {
    #Enter the name of the persons in your contact list along with their WhatsApp numbers as shown below.

    "Mom":"9845XXXXXX",
    "Jack":"7344XXXXXX",
    "Shawn":"8876XXXXXX"

}


def send_whatsapp_message(person, message):
    person_lookup = person.lower().strip()

    if person_lookup in contacts:
        phone_no = contacts[person_lookup]
        try:
            # FIX 1: Increased wait_time to 20 seconds.
            # FIX 2: Set tab_close=False so the browser doesn't close before sending.
            pywhatkit.sendwhatmsg_instantly(f"+{phone_no}", message, wait_time=20, tab_close=False)

            # FIX 3: The Failsafe. Wait 2 seconds after pywhatkit finishes, then force 'Enter'.
            time.sleep(2)
            pyautogui.press('enter')

            return f"Message sent to {person.strip().capitalize()}."
        except Exception as e:
            return f"Error: {e}"
    else:
        return f"I couldn't find '{person_lookup}' in your contacts. I have: {', '.join(contacts.keys())}"


def make_whatsapp_call(person):
    person_lookup = person.lower().strip()
    if person_lookup in contacts:
        phone_no = contacts[person_lookup]
        url = f"https://web.whatsapp.com/send?phone={phone_no}"
        webbrowser.open(url)
        return f"Opening chat with {person.strip().capitalize()}."
    else:
        return f"Contact '{person_lookup}' not found."