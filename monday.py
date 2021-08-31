# pylint: disable=chained-comparison
import os
from sys import argv
import sys
import pyttsx3
import requests
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pyautogui
import PyPDF2
import subprocess
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from mondayUI import Ui_mondayUi


engine = pyttsx3.init('nsss')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I Am Monday Sir. How may i help you!")
    

time = datetime.time().hour

def pdf_reader():
    book = open('.py3.pdf','rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    speak(f"Total number of pages in this book{pages} ")
    speak("sir please enter the page number i have to read")
    pg = int(input("Please enter the page number: "))
    page = pdfReader.getPage(pg)
    text = page.entranceText()
    speak(text)


class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        self.TaskExcution()

    def takeCommand(self):
        #It takes microphone input from the user and returns string output

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source,timeout=5,phrase_time_limit=8)
    
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in' )
            print(f"User said: {query}\n")

        except Exception as e:
            #print(e)
            print("Say that again please...")
            return "None"
        query = query.lower()
        return query

    def TaskExcution(self):
        wishMe()
        while True:
        #if 1:
            self.query = self.takeCommand().lower()

            #Logic for excuting tasks based on query    
            if 'wikipedia' in self.query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to wikipedia")
                print(results) 
                speak(results)

            elif 'open youtube' in self.query:
                webbrowser.open("http://youtube.com")

            elif 'open search' in self.query:
                speak("Sir, what should i search...")
                cm = takeCommand().lower()
                query = f"{cm}"

                r = requests.get("https://api.duckduckgo.com",
                params = {
                "q": query,
                "format": "json"
                })

                data = r.json()

                print(data)
                speak(data["Abstract"])
                print("Abstract")
                print(data["Abstract"])

                

            elif 'open safari' in self.query:
                os.system("open /Applications/Safari.app http://www.google.com")

            elif 'play music' in self.query:
                os.system(f"open ~/Music/songs")
                

            elif 'open gogoanime' in self.query:
                webbrowser.open("http://gogoanime2.org")

            elif 'open code' in self.query:
                os.system("open /Applications/Visual\ Studio\ Code.app")

            elif 'close code' in self.query:
                subprocess.call(['osascript', '-e', 'tell application "Visual Studio Code" to quit'])

            elif 'open Instagram' in self.query:
                webbrowser.open("http://instagram.com")


            elif 'open stack overflow' in self.query:
                webbrowser.open("http://stackoverflow.com")
                

            elif 'open spotify' in self.query:
                os.system("open /Applications/Spotify.app")

            elif 'close spotify' in self.query:
                subprocess.call(['osascript', '-e', 'tell application "Spotify" to quit'])

            elif 'switch the window' in self.query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")

            elif 'exit' in self.query:
                speak("Thanks For using me sir, have a good day.")
                os.sys.exit()

            elif "read pdf" in self.query:
                pdf_reader()

            elif 'where i am' in self.query:
                speak("wait sir,  let me check")
                try:
                    ipAdd = requests.get('https://api.ipify.org').text
                    print(ipAdd)
                    url = f"https://get.geojs.io/v1/ip/geo/{ipAdd}.json"
                    geo_requests = requests.get(url)
                    geo_data = geo_requests.json()
                    #print(geo_data)
                    city = geo_data['city']
                    #state
                    country = geo_data['country']
                    speak(f"sir i am not sure, i think we are in{city} city of {country} country")
                except Exception as e:
                    speak("sorry sir, Due to network issue i am not able to find where we are")
                    pass


startExcution = MainThread() 

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_mondayUi()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("../../Downloads/7LP8.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.start()
        self.ui.movie = QtGui.QMovie("../../Downloads/T8bahf.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExcution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)

app = QApplication(sys.argv)
monday = Main()
monday.show()
exit(app.exec_())






        


        

        

        


            
        
        
