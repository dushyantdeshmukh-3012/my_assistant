import engine
from skills import info_skill, browser_skill, whatsapp_skill


def run_assistant(ui):
    # Using our new Cyber-Cyan accent color code: #00e6e6
    engine.speak("All systems functional. Assistant is ready.")

    while True:
        ui.update_status("Listening...", "#FFFF00")  # Yellow
        command = engine.listen()

        if command == "none":
            ui.update_status("Idle", "gray")
            continue

        ui.update_status(f"Heard: {command}", "#00e6e6")  # Cyber-Cyan

        # --- 1. YOUTUBE SKILL ---
        if 'play' in command:
            song = command.replace('play', '').strip()
            if song:
                ui.show_info(f"ACTION: Playing YouTube\nSONG: {song}")
                engine.speak(f"Playing {song} on YouTube")
                browser_skill.play_on_youtube(song)
            else:
                engine.speak("What would you like me to play?")

        # --- 2. CHROME / GOOGLE SEARCH ---
        elif 'search' in command:
            query = command.replace('search', '').strip()
            if query:
                ui.show_info(f"ACTION: Google Search\nQUERY: {query}")
                engine.speak(f"Searching Google for {query}")
                browser_skill.search_google(query)
            else:
                engine.speak("What should I search for?")

        # --- 3. WIKIPEDIA (Einstein Example) ---
        elif any(trigger in command for trigger in ['who is', 'what is', 'tell me about']):
            topic = command.replace('who is', '').replace('what is', '').replace('tell me about', '').strip()
            if topic:
                ui.update_status("Searching Wikipedia...", "#00e6e6")
                # info_skill returns screen_txt (formatted) and voice_txt (clean summary)
                screen_txt, voice_txt = info_skill.search_wikipedia(topic)

                ui.show_info(screen_txt)  # Display on fullscreen
                engine.speak(voice_txt)  # READ ALOUD to the user
            else:
                engine.speak("What should I search for?")

        # --- 4. WHATSAPP MESSAGE ---
        elif 'send' in command and ' to ' in command and 'start' in command:
            try:
                person = command.split(' to ')[1].split('start')[0].strip()
                if 'stop' in command:
                    start_idx = command.find('start') + len('start')
                    stop_idx = command.find('stop')
                    message_content = command[start_idx:stop_idx].strip()

                    ui.show_info(f"WHATSAPP OUTGOING\nTo: {person.upper()}\nMsg: {message_content}")
                    engine.speak(f"Sending message to {person}")
                    result = whatsapp_skill.send_whatsapp_message(person, message_content)
                    engine.speak(result)
                else:
                    engine.speak("I heard the start keyword, but you didn't say stop.")
            except Exception as e:
                engine.speak("I couldn't understand the WhatsApp format.")

        # --- 5. WHATSAPP CALL ---
        elif 'call' in command:
            person = command.replace('call', '').strip()
            if person:
                ui.show_info(f"WHATSAPP CALL\nTarget: {person}")
                engine.speak(f"Opening WhatsApp call for {person}")
                result = whatsapp_skill.make_whatsapp_call(person)
                engine.speak(result)
            else:
                engine.speak("Who should I call?")

        # --- 6. TIME & DATE ---
        elif 'time' in command:
            screen_txt, voice_txt = info_skill.get_time()
            ui.show_info(screen_txt)
            engine.speak(voice_txt)  # READ ALOUD

        elif 'date' in command:
            screen_txt, voice_txt = info_skill.get_date()
            ui.show_info(screen_txt)
            engine.speak(voice_txt)  # READ ALOUD

        # --- 7. NEW: REPEAT/READ SCREEN ---
        elif 'read' in command and 'screen' in command:
            # Grabs the current text from the UI display box
            current_text = ui.display_box.get("0.0", "end").strip()
            if current_text and "Waiting" not in current_text:
                engine.speak("Okay, reading the display for you.")
                engine.speak(current_text)
            else:
                engine.speak("The screen is currently empty.")

        # --- 8. EXIT ---
        elif any(word in command for word in ['stop assistant', 'exit', 'offline']):
            engine.speak("Goodbye!")
            ui.update_status("Offline", "red")
            break

        else:
            ui.show_info("Unknown command.")
            engine.speak("I didn't quite catch that.")