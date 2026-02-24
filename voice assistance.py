import pywhatkit
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
          print('Listening...')
          voices = listener.listen(source)
          command = listener.recognize_google(voices)
          command = command.lower()
          if 'alexa' in command:
              command = command.replace('alexa', '')
              print(command)
          return command
    except Exception as e:
        print(f"Error: {e}")
        return ""


def run_alexa():
    command = take_command()
    print(command)
    if command and 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('current time is ' + time)
    elif 'information' in command:
        person = command.replace('wikipedia', '').strip()  # Remove 'wikipedia' keyword
        if not person:  # No name provided
            talk("I couldn't recognize the person. Please specify a name.")
            return

        try:
            info = wikipedia.summary(person, sentences=1)
            print(info)  # Print to console for debugging
            talk(info)  # Speak the result
        except wikipedia.exceptions.PageError:
            talk("Sorry, I couldn't find any information on Wikipedia for that person.")
        except wikipedia.exceptions.DisambiguationError as e:
            talk("There are multiple results for that name. Please be more specific.")
            print(f"DisambiguationError options: {e.options}")  # Debugging output
        except Exception as e:
            talk("An error occurred while fetching information from Wikipedia.")
            print(f"Error: {e}")

    elif 'linkedin' in command:
        talk("Opening LinkedIn")
        webbrowser.open("https://www.linkedin.com")
    elif 'github' in command:
        talk("Opening Github")
        webbrowser.open("https://github.com")
    elif 'google' in command:
        webbrowser.open("https://www.google.com")
        talk("Opening Google")

    elif 'facebook' in command:
        webbrowser.open("https://www.facebook.com")
        talk("Opening Facebook")
    elif 'twitter' in command:
        webbrowser.open("https://twitter.com")
        talk("Opening Twitter")
    elif 'instagram' in command:
        webbrowser.open("https://www.instagram.com")
        talk("Opening Instagram")
    if command and 'visual studio code' in command:  # Lowercase to match
        webbrowser.open("https://code.visualstudio.com")
        talk("Opening Visual Studio Code")
    elif command and 'jokes' in command:
        talk(pyjokes.get_joke())
        print(pyjokes.get_joke())

    else:
        talk("Sorry, I didn't understand that command.")

run_alexa()