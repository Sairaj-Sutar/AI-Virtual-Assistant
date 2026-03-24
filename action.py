
import speech_to_text
import datetime
import speak
import webbrowser
import os
import subprocess
import fnmatch
import pyautogui
import pyperclip


# -------------------------------
# Smart File Finder Function
# -------------------------------

clipboard_history = []

def track_clipboard():

    text = pyperclip.paste()

    if text not in clipboard_history:
        clipboard_history.append(text)

    if len(clipboard_history) > 10:
        clipboard_history.pop(0)

def smart_file_finder(filename):

    search_paths = [
        "C:\\Users\\hp\\Desktop",
        "C:\\Users\\hp\\Documents",
        "C:\\Users\\hp\\Downloads"
    ]

    for path in search_paths:
        for root, dirs, files in os.walk(path):
            for file in files:
                if fnmatch.fnmatch(file.lower(), "*" + filename.lower() + "*"):
                    file_path = os.path.join(root, file)
                    os.startfile(file_path)
                    return file_path

    return None

def save_note(note_text):

    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(".venv/notes.txt", "a") as file:
        file.write(f"[{time}] {note_text}\n")

# -------------------------------
# Assistant Action Function
# -------------------------------
def Action(send):

    data_btn = send.lower()

    # Greetings
    if "what is your name" in data_btn:
        speak.speak("My name is Virtual Assistant")
        return "My name is Virtual Assistant"

    elif "hello" in data_btn or "hye" in data_btn or "hay" in data_btn:
        speak.speak("Hey sir, How can I help you!")
        return "Hey sir, How can I help you!"

    elif "how are you" in data_btn:
        speak.speak("I am doing great these days, sir")
        return "I am doing great these days, sir"

    elif "thanku" in data_btn or "thank" in data_btn:
        speak.speak("It's my pleasure, sir, to stay with you")
        return "It's my pleasure, sir, to stay with you"

    elif "good morning" in data_btn:
        speak.speak("Good morning sir, I think you might need some help")
        return "Good morning sir, I think you might need some help"

    # Time
    elif "time now" in data_btn:
        current_time = datetime.datetime.now()
        Time = f"{current_time.hour} Hour : {current_time.minute} Minute"
        speak.speak(Time)
        return Time


    # Music
    elif "play music" in data_btn or "song" in data_btn:
        webbrowser.open("https://gaana.com/")
        speak.speak("gaana.com is now ready for you, enjoy your music")
        return "gaana.com is now ready for you, enjoy your music"

    elif "music from my laptop" in data_btn:
        url = 'D:\\music'
        songs = os.listdir(url)
        os.startfile(os.path.join(url, songs[0]))
        speak.speak("Song playing...")
        return "Song playing..."


    # Websites
    elif "open google" in data_btn:
        webbrowser.open("https://google.com/")
        speak.speak("Google is open now")
        return "Google is open now"

    elif "youtube" in data_btn or "open youtube" in data_btn:
        webbrowser.open("https://youtube.com/")
        speak.speak("YouTube is open now")
        return "YouTube is open now"

    elif "play netflix" in data_btn or "movie" in data_btn:
        webbrowser.open("https://netflix.com/")
        speak.speak("Netflix is now ready for you, enjoy your movies")
        return "Netflix is now ready for you, enjoy your movies"

    elif "open whatsapp" in data_btn:
        webbrowser.open("https://whatsapp.com/")
        speak.speak("WhatsApp is now ready for you, sir")
        return "WhatsApp is now ready for you, sir"


    # Applications
    elif "open word" in data_btn:
        subprocess.run(["start", "winword"], shell=True)
        speak.speak("Microsoft Word is now ready for you, sir")
        return "Microsoft Word is now ready for you, sir"

    elif "open calculator" in data_btn:
        subprocess.run(["start", "calc"], shell=True)
        speak.speak("Calculator is now ready for you, sir")
        return "Calculator is now ready for you, sir"

    elif "open notepad" in data_btn:
        subprocess.run(["start", "notepad"], shell=True)
        speak.speak("Notepad is now ready for you, sir")
        return "Notepad is now ready for you, sir"

    elif "search" in data_btn:

        query = data_btn.replace("search", "").strip()

        if query != "":
            url = "https://www.google.com/search?q=" + query.replace(" ", "+")
            webbrowser.open(url)

            speak.speak("Searching Google for " + query)

            return "Searching Google for " + query


    elif "take screenshot" in data_btn:

        speak.speak("Taking screenshot")

        time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

        filename = f"screenshot_{time}.png"

        screenshot = pyautogui.screenshot()

        screenshot.save(filename)

        speak.speak("Screenshot saved")

        return f"Screenshot saved as {filename}"

    #
    # # Smart File Finder
    # elif "find file" in data_btn or "search file" in data_btn or "open file" in data_btn:
    #
    #     speak.speak("Please tell the file name")
    #
    #     filename = speech_to_text.speech_to_text()
    #
    #     speak.speak("Searching for the file")
    #
    #     result = smart_file_finder(filename)
    #
    #     if result:
    #         speak.speak("File found and opening now")
    #         return f"File found: {result}"
    #
    #     else:
    #         speak.speak("Sorry sir, file not found")
    #         return "File not found"

    elif "find file" in data_btn or "search file" in data_btn or "open file" in data_btn:

        # extract filename from command
        filename = data_btn.replace("find file", "").replace("search file", "").replace("open file", "").strip()

        speak.speak("Searching for the file")

        result = smart_file_finder(filename)

        if result:
            speak.speak("File found and opening now")
            return f"File found: {result}"
        else:
            speak.speak("Sorry sir, file not found")
            return "File not found"

    elif "create note" in data_btn or "take note" in data_btn:

        speak.speak("What should I write")

        note = speech_to_text.speech_to_text()

        save_note(note)

        speak.speak("Note saved successfully")

        return "Note saved successfully"

    elif "show notes" in data_btn or "show my notes" in data_btn:

        os.startfile(".venv/notes.txt")

        speak.speak("Opening your notes")

        return "Opening your notes"

    elif "clipboard history" in data_btn or "show clipboard" in data_btn:

        track_clipboard()

        if clipboard_history:

            result = "\n".join(clipboard_history)

            speak.speak("Here is your clipboard history")

            return result

        else:
            speak.speak("Clipboard is empty")

            return "Clipboard is empty"




    # Default
    else:
        speak.speak("I'm not able to understand that command!")
        return "I'm not able to understand that command!"