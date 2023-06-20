import pyttsx3
import speech_recognition as sr

# Initialize the speech engine
engine = pyttsx3.init()

# Set the properties of the speech engine
engine.setProperty('rate', 150)
engine.setProperty('volume', 1)

# Define a function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Define a function to listen for speech
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said:", text)
        return text
    except:
        print("Sorry, I didn't catch that.")
        return ""

# Define the main function
def main():
    speak("Hello! How can I help you today?")
    while True:
        text = listen().lower()
        if "hello" in text:
            speak("Hi there!")
        elif "goodbye" in text:
            speak("Goodbye!")
            break
        else:
            speak("I'm sorry, I don't understand. Can you say that again?")

if __name__ == '__main__':
    main()
