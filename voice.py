import speech_recognition as sr  # recognise speech
import playsound  # to play an audio files
from gtts import gTTS  # google text to speech
import random
import smtplib
from email.message import EmailMessage
from time import ctime  # get time details
import webbrowser  # open browser

import time
from PIL import Image
import pyautogui  # screenshot
import pyttsx3
import bs4 as bs
import urllib.request


class person:
    name = ''

    def setName(self, name):
        self.name = name


class asis:
    name = ''

    def setName(self, name):
        self.name = name


def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True


def engine_speak(text):
    text = str(text)
    engine.say(text)
    engine.runAndWait()


r = sr.Recognizer()  # initialise a recogniser
engine = pyttsx3.init()
voices = engine.getProperty('voices')

engine.setProperty('volume',9) #volume level 0 to 1
engine.setProperty('voice',voices[1].id)# 2 type of voices male and female (voice.id)

# listen for audio and convert it to text:
def record_audio(ask=""):
    with sr.Microphone() as source:  # microphone as source
        if ask:
            engine_speak(ask)
        audio = r.listen(source, 5, 5)  # listen for the audio via source
        print("Done Listening")
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)  # convert audio to text
        except sr.UnknownValueError:  # error: recognizer does not understand
            engine_speak('I did not get that')
        except sr.RequestError:
            engine_speak('Sorry, the service is down')  # error: recognizer is not connected
        print(">>", voice_data.lower())  # print what user said
        return voice_data.lower()




def respond(voice_data):
    # 1: greeting
    if there_exists(['hey', 'hi', 'hello']):
        greetings = ["hey, how can I help you" + person_obj.name, "hey, what's up?" + person_obj.name,
                     "I'm listening" + person_obj.name, "how can I help you?" + person_obj.name,
                     "hello" + person_obj.name]
        greet = greetings[random.randint(0, len(greetings) - 1)]
        engine_speak(greet)

    # 2: name
    if there_exists(["what is your name", "what's your name", "tell me your name"]):
        if person_obj.name:
            engine_speak("I'm Mini, Your personal asisstant ")
        else:
            engine_speak("I'm Mini. what's your name?")

    if there_exists(["my name is"]):
        person_name = voice_data.split("is")[-1].strip()
        engine_speak("okay, i will remember that " + person_name)
        person_obj.setName(person_name)  # remember name in person object



    # 3: greeting
    if there_exists(["how are you", "how are you doing"]):
        engine_speak("I'm very well, thanks for asking " + person_obj.name)

    # 4: time
    if there_exists(["what's the time", "tell me the time", "what time is it"]):
        time = ctime().split(" ")[3].split(":")[0:2]
        if time[0] == "00":
            hours = '12'
        else:
            hours = time[0]
        minutes = time[1]
        time = hours + " hours and " + minutes + "minutes"
        engine_speak(time)

    # 5: search google
    if there_exists(["search for"]) and 'youtube' not in voice_data:
        search_term = voice_data.split("for")[-1]
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for" + search_term + "on google")

    # 6: search youtube
    if there_exists(["youtube"]):
        search_term = voice_data.split("for")[-1]
        url = "https://www.youtube.com/results?search_query=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for " + search_term + "on youtube")

    # 7: get stock price
    if there_exists(["price of"]):
        search_term = voice_data.split("for")[-1]
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for " + search_term + " on google")

    # search for music
    if there_exists(["play music"]):
        search_term = voice_data.split("for")[-1]
        url = "https://open.spotify.com/search/" + search_term
        webbrowser.get().open(url)
        engine_speak("You are listening to" + search_term + "enjoy sir")
    # search for amazon.com
    if there_exists(["amazon.com"]):
        search_term = voice_data.split("for")[-1]
        url = "https://www.amazon.in" + search_term
        webbrowser.get().open(url)
        engine_speak("here is what i found for" + search_term + "on amazon.com")

    # make a note
    if there_exists(["make a note"]):
        search_term = voice_data.split("for")[-1]
        url = "https://keep.google.com/#home"
        webbrowser.get().open(url)
        engine_speak("Here you can make notes")

    # open instagram
    if there_exists(["open instagram", "want to have some fun time"]):
        search_term = voice_data.split("for")[-1]
        url = "https://www.instagram.com/"
        webbrowser.get().open(url)
        engine_speak("opening instagram")




    # open twitter
    if there_exists(["open twitter"]):
        search_term = voice_data.split("for")[-1]
        url = "https://twitter.com/"
        webbrowser.get().open(url)
        engine_speak("opening twitter")

    # 8 time table
    if there_exists(["show my time table"]):
        im = Image.open(r"D:\WhatsApp Image 2019-12-26 at 10.51.10 AM.jpeg")
        im.show()

    # 9 weather
    if there_exists(["weather", "tell me the weather report", "whats the condition outside"]):
        search_term = voice_data.split("for")[-1]
        url = "https://www.google.com/search?sxsrf=ACYBGNSQwMLDByBwdVFIUCbQqya-ET7AAA%3A1578847393212&ei=oUwbXtbXDN-C4-EP-5u82AE&q=weather&oq=weather&gs_l=psy-ab.3..35i39i285i70i256j0i67l4j0i131i67j0i131j0i67l2j0.1630.4591..5475...1.2..2.322.1659.9j5j0j1......0....1..gws-wiz.....10..0i71j35i39j35i362i39._5eSPD47bv8&ved=0ahUKEwiWrJvwwP7mAhVfwTgGHfsNDxsQ4dUDCAs&uact=5"
        webbrowser.get().open(url)
        engine_speak("Here is what I found for on google")

    # open gmail
    if there_exists(["open my mail", "gmail", "check my email"]):
        search_term = voice_data.split("for")[-1]
        url = "https://mail.google.com/mail/u/0/#inbox"
        webbrowser.get().open(url)
        engine_speak("here you can check your gmail")

    # 10 stone paper scisorrs

    if there_exists(["game"]):
        voice_data = record_audio("choose among rock paper or scissor")
        moves = ["rock", "paper", "scissor"]

        cmove = random.choice(moves)
        pmove = voice_data

        engine_speak("The computer chose " + cmove)
        engine_speak("You chose " + pmove)
        # engine_speak("hi")
        if pmove == cmove:
            engine_speak("the match is draw")
        elif pmove == "rock" and cmove == "scissor":
            engine_speak("Player wins")
        elif pmove == "rock" and cmove == "paper":
            engine_speak("Computer wins")
        elif pmove == "paper" and cmove == "rock":
            engine_speak("Player wins")
        elif pmove == "paper" and cmove == "scissor":
            engine_speak("Computer wins")
        elif pmove == "scissor" and cmove == "paper":
            engine_speak("Player wins")
        elif pmove == "scissor" and cmove == "rock":
            engine_speak("Computer wins")

    # 11 toss a coin
    if there_exists(["toss", "flip", "coin"]):
        moves = ["head", "tails"]
        cmove = random.choice(moves)
        engine_speak("The computer chose " + cmove)

    # 12 calc
    if there_exists(["plus", "minus", "multiply", "divide", "power", "+", "-", "*", "/"]):
        opr = voice_data.split()[1]

        if opr == '+':
            engine_speak(int(voice_data.split()[0]) + int(voice_data.split()[2]))
        elif opr == '-':
            engine_speak(int(voice_data.split()[0]) - int(voice_data.split()[2]))
        elif opr == 'multiply':
            engine_speak(int(voice_data.split()[0]) * int(voice_data.split()[2]))
        elif opr == 'divide':
            engine_speak(int(voice_data.split()[0]) / int(voice_data.split()[2]))
        elif opr == 'power':
            engine_speak(int(voice_data.split()[0]) ** int(voice_data.split()[2]))
        else:
            engine_speak("Wrong Operator")

    # 13 screenshot
    if there_exists(["capture", "my screen", "screenshot"]):
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save('C:/Users/LUCIFER/Desktop')

        # 14 to search wikipedia for definition
    if there_exists(["definition of"]):
        definition = record_audio("what do you need the definition of")
        url = urllib.request.urlopen('https://en.wikipedia.org/wiki/' + definition)
        soup = bs.BeautifulSoup(url, 'lxml')
        definitions = []
        for paragraph in soup.find_all('p'):
            definitions.append(str(paragraph.text))
        if definitions:
            if definitions[0]:
                engine_speak('im sorry i could not find that definition, please try a web search')
            elif definitions[1]:
                engine_speak('here is what i found ' + definitions[1])
            else:
                engine_speak('Here is what i found ' + definitions[2])
        else:
            engine_speak("im sorry i could not find the definition for " + definition)

    if there_exists(["exit", "quit", "goodbye"]):
        engine_speak("we could continue more sir, but.,,...,,,,,..,,,,, byee")
        exit()

# Sending mail
    if there_exists(["send mail", "open email"]):
        def get_info():
            try:
                with sr.Microphone() as source:
                    print('listening...')
                    engine.setProperty('rate', 150)

                    voice = r.listen(source)
                    info = r.recognize_google(voice)
                    print(info)
                    return info.lower()
            except:
                pass
        def send_email(receiver, subject, message):
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()

            server.login('manojkumarmanju1709@gmail.com', '9177291956')
            email = EmailMessage()
            email['From'] = 'Sender_Email'
            email['To'] = receiver
            email['Subject'] = subject
            email.set_content(message)
            server.send_message(email)

        email_list = {
            'manoj': 'manojmanju1709@gmail.com',
            'manojkumar': 'manojkumarmanju17@gmail.com',

        }

        def get_email_info():
            engine_speak('Hi Sir I am your assistant for today, To Whom you want to send email')
            name = get_info()
            receiver = email_list[name]
            print(receiver)
            engine_speak('What is the subject of your email?')
            subject = get_info()
            engine_speak('Tell me the text in your email')
            message = get_info()
            send_email(receiver, subject, message)
            engine_speak('Thankyou sir for using me. Your email has been send')
            engine_speak('Do you want to send more email?')
            send_more = get_info()
            if 'yes' in send_more:
                get_email_info()

        get_email_info()

#finding book in library
    if there_exists(["find me a book", "Need a book"]):
        def get_info():
            try:
                with sr.Microphone() as source:
                    print('listening...')

                    voice = r.listen(source)
                    info = r.recognize_google(voice)
                    print(info)
                    return info.lower()
            except:
                pass

        rack = {101: {'shelf1': {'Data Structures': {1:'Data Structures and Algorithmic Thinking with Go - Author Narasimha Karumanchi',
                                           2:'Data Structures And Algorithms Made Easy: Data Structures And Algorithmic Puzzles - Author Narasimha Karumanchi '},
                      'Artificial Intelligence':{1:'Artificial Intelligence - Third Edition - By Pearson: A Modern Approach Author Russell',
                                                   2:'Essentials of Artificial Intelligence - Author  Kartik Sharma '}

                       }}}



        def get_bookname_info():
            engine_speak('Hi Sir I am your assistant for today, Which book do you need ')
            bookname = get_info()
            if (rack[101]['shelf1'] == 'bookname'):
                print(rack[101]['shelf1'])

            engine_speak(rack[101]['shelf1'])

        get_bookname_info()


time.sleep(1)

person_obj = person()
asis_obj = asis()
asis_obj.name = 'Mini'


while (1):
    voice_data = record_audio("How may I help you?")  # get the voice input
    print("Done")
    print("Q:", voice_data)
    respond(voice_data)  # respond