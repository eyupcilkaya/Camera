from datetime import datetime
import cv2
from pyrebase import pyrebase
import firebaseConfigFile
import variables

cap = cv2.VideoCapture(0)
firebase = pyrebase.initialize_app(firebaseConfigFile.firebaseConfig)
storage = firebase.storage()

def Camera():
    a = datetime.now()
    while (True):
        i=0
        while i<10:
            b=datetime.now()
            ret, frame = cap.read()
            if (b - a).microseconds >= 500000 :
                a = b
                img="resim/{}.jpg".format(i)
                cv2.imwrite(f"{img}", frame, [cv2.IMWRITE_JPEG_QUALITY, 50])
                s=variables.camera_data()
                s.set_cam_data(img)
                i=i+1




