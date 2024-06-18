import os
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import subprocess
import webbrowser
import requests
from bs4 import BeautifulSoup
import threading
import pyautogui
import time
import tkinter as tk
from tkinter import messagebox

# Initialize the speech recognizer and text-to-speech engine
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    command = ""
    try:
        with sr.Microphone() as source:
            print('Listening...')
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '').strip()
                print(command)
    except sr.UnknownValueError:
        pass
    except sr.RequestError:
        pass
    return command

def get_weather(city):
    try:
        url = f'https://www.weather.com/weather/today/l/{city}'
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            weather_conditions = soup.find(class_='CurrentConditions--phraseValue--2xXSr').get_text()
            temperature = soup.find(class_='CurrentConditions--tempValue--3KcTQ').get_text()
            return f"The weather in {city} today is {weather_conditions} with a temperature of {temperature} degrees Celsius."
        else:
            return None
    except Exception as e:
        return None

# Global state variables to track context
youtube_open = False
youtube_search_done = False
command_executed = False
running = False

def run_alexa():
    global youtube_open, youtube_search_done, command_executed, running
    talk("Hey, I'm Alexa. How can I assist you?")
    while running:
        command = take_command()
        if command:
            command_executed = True
            print(command)
            if 'play' in command:
                song = command.replace('play', '').strip()
                talk('playing ' + song)
                threading.Thread(target=pywhatkit.playonyt, args=(song,)).start()
            elif 'time' in command:
                time = datetime.datetime.now().strftime('%I:%M %p')
                talk('Current time is ' + time)
            elif 'who is' in command:
                person = command.replace('who is', '').strip()
                try:
                    info = wikipedia.summary(person, 1)
                    print(info)
                    talk(info)
                except wikipedia.exceptions.DisambiguationError as e:
                    talk(f"There are multiple results for {person}. Can you please be more specific?")
            elif 'date' in command:
                talk('Sorry, I have a headache.')
            elif 'are you single' in command:
                talk('I am in a relationship with wifi.')
            elif 'joke' in command:
                talk(pyjokes.get_joke())
            elif 'open google chrome' in command:
                talk('Opening Google Chrome.')
                threading.Thread(target=subprocess.Popen, args=(['C:/Program Files/Google/Chrome/Application/chrome.exe'],)).start()
            elif 'open youtube' in command:
                talk('Opening YouTube.')
                youtube_open = True
                youtube_search_done = False
                threading.Thread(target=webbrowser.open, args=('https://www.youtube.com',)).start()
            elif 'search' in command and 'youtube' in command and youtube_open:
                search_query = command.replace('search', '').replace('youtube', '').strip()
                talk(f'Searching {search_query} on YouTube.')
                youtube_search_done = True
                threading.Thread(target=pywhatkit.playonyt, args=(search_query,)).start()
            elif 'search' in command and 'google' in command:
                search_query = command.replace('search', '').replace('google', '').strip()
                talk(f'Searching {search_query} on Google.')
                threading.Thread(target=pywhatkit.search, args=(search_query,)).start()
            elif 'open' in command and 'website' in command:
                website = command.replace('open', '').replace('website', '').strip()
                talk(f'Opening {website}.')
                threading.Thread(target=webbrowser.open, args=(f'http://{website}',)).start()
            elif 'open vscode' in command or 'open visual studio code' in command:
                talk('Opening Visual Studio Code.')
                threading.Thread(target=subprocess.Popen, args=(['C:/path/to/your/vscode.exe'],)).start()
            elif 'open my computer' in command:
                talk('Opening File Explorer.')
                threading.Thread(target=subprocess.Popen, args=(['explorer'],)).start()
            elif 'open' in command and 'video' in command and youtube_open and youtube_search_done:
                try:
                    video_number = int(command.replace('open video', '').strip())
                    talk(f'Opening video number {video_number} on YouTube.')
                    threading.Thread(target=open_youtube_video, args=(video_number,)).start()
                except ValueError:
                    talk('Please specify a valid number for the video.')
            elif 'weather today in' in command:
                city = command.split('in')[-1].strip()
                weather_data = get_weather(city)
                if weather_data:
                    talk(weather_data)
                else:
                    talk("Sorry, I couldn't fetch the weather data for that location.")
            elif 'shutdown' in command:
                talk('Shutting down the system. Goodbye!')
                os.system("shutdown /s /t 1")
            elif 'restart' in command:
                talk('Restarting the system. See you in a moment!')
                os.system("shutdown /r /t 1")
            elif 'thank you for today' in command:
                talk('You are welcome! Have a great day!')
                break
            else:
                talk("I'm not sure what you mean. Can you please clarify?")
        elif not command_executed:
            talk("Sorry, I didn't get that. Can you please repeat?")
            command_executed = True

def open_youtube_video(video_number):
    time.sleep(2)  # Allow some time for the page to load
    for _ in range(video_number):
        pyautogui.press('tab')
    pyautogui.press('enter')

def start_alexa():
    global running
    running = True
    threading.Thread(target=run_alexa).start()

def stop_alexa():
    global running
    running = False
    talk("Stopping the assistant. Goodbye!")
    root.destroy()

# GUI setup
root = tk.Tk()
root.title("Alexa Voice Assistant")

start_button = tk.Button(root, text="Start", command=start_alexa)
start_button.pack(pady=20)

stop_button = tk.Button(root, text="Stop", command=stop_alexa)
stop_button.pack(pady=20)

root.mainloop()
