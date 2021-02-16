from _datetime import datetime
from pyrebase import pyrebase
import firebaseConfigFile
from variables import Variables
import cv2

firebase=pyrebase.initialize_app(firebaseConfigFile.firebaseConfig)
storage = firebase.storage()

def upload(var_data):

    a = datetime.now()

    while (True):
        b=datetime.now()

        if (b-a).seconds>=1:
            a=b
            img = var_data.get_cam_data()

            if img != "":
                storage.child("1.jpg").put("{}".format(img))
                print("IMG is not null")