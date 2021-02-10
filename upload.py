from datetime import datetime
import cv2
from pyrebase import pyrebase
import firebaseConfigFile
import RPi.GPIO as io
import threading

io.setmode(io.BCM)
powerpin = 23

io.setup(powerpin, io.OUT)
io.output(powerpin, False)

firebase = pyrebase.initialize_app(firebaseConfigFile.firebaseConfig)
db = firebase.database()

cap = cv2.VideoCapture(0)
storage = firebase.storage()


def Camera():
    a = datetime.now()
    while (True):
        ret, frame = cap.read()
        b = datetime.now()
        try:
            if (b - a).microseconds > 600000:
                a = b
                cv2.imwrite("1.jpg", frame)
                storage.child("1.jpg").put("1.jpg")
        except:
            continue


def Role():
    while (True):

        data = db.child("Role").get()
        role = data.val()
        if role == "1":
            io.output(powerpin, True)
        else:
            io.output(powerpin, False)


camThread = threading.Thread(target=Camera)
roleThread = threading.Thread(target=Role)

camThread.start()
roleThread.start()









