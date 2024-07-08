# Alexa Voice Assistant

## Overview
This Python program implements a voice-controlled assistant similar to Amazon Alexa. It allows users to interact via voice commands to perform various tasks such as playing music on YouTube, retrieving information from Wikipedia, fetching weather updates, and more.

## Features
- **Voice Recognition**: Utilizes the SpeechRecognition library to recognize voice commands.
- **Text-to-Speech**: Employs pyttsx3 for converting text responses into audible speech.
- **Web Interaction**: Uses web scraping and web browser automation for tasks like fetching weather data and opening websites.
- **Multithreading**: Implements threading for handling multiple tasks simultaneously, like playing YouTube videos in the background.
- **GUI Interface**: Includes a basic GUI using tkinter for starting and stopping the assistant.

## Dependencies
- Python 3.x
- Libraries:
  - speech_recognition
  - pyttsx3
  - pywhatkit
  - wikipedia
  - pyjokes
  - BeautifulSoup (bs4)
  - requests
  - tkinter
  - pyautogui (for automating GUI interactions)

## Usage
1. **Installation**:
   - Ensure Python 3.x is installed.
   - Install required libraries using pip:
     ```
     pip install speech_recognition pyttsx3 pywhatkit wikipedia pyjokes beautifulsoup4 requests pyautogui
     ```

2. **Execution**:
   - Run the `app.py` script.
   - Click the "Start" button in the GUI to activate the assistant.
   - Speak commands prefixed with "Alexa" (e.g., "Alexa, play music").

3. **Voice Commands**:
   - **Basic Commands**: Ask for time, tell jokes, inquire about someone via Wikipedia, etc.
   - **Media Commands**: Play music on YouTube, open specific videos, search Google or YouTube.
   - **System Commands**: Open applications like Visual Studio Code or File Explorer, shutdown or restart the system.

4. **Stopping**:
   - Click the "Stop" button in the GUI to terminate the assistant.
     
## Acknowledgments
- Inspired by virtual assistants like Amazon Alexa.
- Uses various Python libraries for voice recognition, web interaction, and GUI development.

## Link :  - https://saptarshi2060.github.io/Portfolio/responsive_portfolio/index.html
