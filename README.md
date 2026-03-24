# AI Virtual Assistant

A desktop-based AI virtual assistant built using Python and Tkinter that performs tasks using voice commands and provides interactive responses.

---

## Features

* Voice command recognition
* Text-to-speech responses (pyttsx3)
* GUI using Tkinter
* Web search and  automation
* Fast and lightweight

---

## Tech Stack

* Python
* Tkinter
* Libraries: pyttsx3, SpeechRecognition, PyAudio

---

## Setup & Run

1. Clone the repository

```bash id="n1"
git clone https://github.com/Sairaj-Sutar/AI-Virtual-Assistant.git
cd AI-Virtual-Assistant
```

2. Install dependencies

```bash id="n2"
pip install pyttsx3 SpeechRecognition pyaudio
```

If PyAudio error comes:

```bash id="n3"
pip install pipwin
pipwin install pyaudio
```

3. Run the project

```bash id="n4"
python main.py
```

---

## Project Structure

```id="n5"
AI-Virtual-Assistant/
│── main.py
│── assistant.py
│── assets/
│── README.md
```

---

## Challenges Faced

* PyAudio installation issues on Windows
* Handling background noise in voice recognition
* Improving accuracy of speech commands
* Managing real-time response speed
* Integrating GUI with voice processing

---

## Use Cases

* Personal assistant
* Task automation
* Voice-controlled system

---

## Future Scope

* AI integration (ChatGPT)
* Mobile app version
* API integration (weather, news)

---

## Author

Sairaj Sutar
https://github.com/Sairaj-Sutar

---

Star this repository if you like it.
