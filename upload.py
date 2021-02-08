from datetime import datetime
import cv2
from pyrebase import pyrebase
import firebaseConfigFile

cap = cv2.VideoCapture(0)

firebase=pyrebase.initialize_app(firebaseConfigFile.firebaseConfig)
storage = firebase.storage()
a=datetime.now()
while(True):
    ret,frame=cap.read()
    cv2.imwrite("resim.jpg",frame)
    b = datetime.now()
    cv2.imshow("Camera", frame)
    if ((b - a).seconds >= 0.001):
        a = b
        storage.child("1.jpg").put("resim.jpg")
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
