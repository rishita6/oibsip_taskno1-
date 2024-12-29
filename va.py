import speech_recognition as sr
import pyttsx3
import webbrowser
from datetime import datetime


# Initialize the speech engine
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def get_audio():
    """Capture voice input and convert it to text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            speak("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            print("Service is down. Please try again later.")
            speak("Service is down. Please try again later.")
            return ""

def respond_to_command(command):
    """Process and respond to user commands."""
    if "hello" in command:
        speak("Hello! How can I assist you today?")
    elif "time" in command:
        current_time = datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}.")
    elif "date" in command:
        current_date = datetime.now().strftime("%B %d, %Y")
        speak(f"Today's date is {current_date}.")
    elif "search" in command:
        speak("What should I search for?")
        query = get_audio()
        if query:
            url = f"https://www.google.com/search?q={query}"
            webbrowser.open(url)
            speak(f"Here are the search results for {query}.")
    elif "exit" in command or "quit" in command:
        speak("Goodbye! Have a great day!")
        exit()
    else:
        speak("I'm sorry, I can't help with that yet.")

if __name__ == "__main__":
    speak("Starting the voice assistant. Say 'hello' to begin.")
    while True:
        command = get_audio()
        if command:
            respond_to_command(command)
