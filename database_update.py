from _datetime import datetime
from pyrebase import pyrebase
import firebaseConfigFile
import variables

firebase=pyrebase.initialize_app(firebaseConfigFile.firebaseConfig)
storage = firebase.storage()

def upload():

    s = variables.camera_data()
    a=datetime.now()

    while (True):

        b=datetime.now()

        if (b-a).seconds>=1:
            a=b
            img = s.get_cam_data()

            if img != "":
                storage.child("1.jpg").put("{}".format(img))