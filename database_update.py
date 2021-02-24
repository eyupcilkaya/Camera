from _datetime import datetime
from pyrebase import pyrebase
import firebaseConfigFile

firebase=pyrebase.initialize_app(firebaseConfigFile.firebaseConfig)
storage = firebase.storage()
db = firebase.database()


def update(var_data):

    a = datetime.now()

    while True:
        b = datetime.now()

        if (b-a).seconds >= 1:
            a = b
            img = var_data.get_cam_data()

            if img != "":
                storage.child("1.jpg").put("{}".format(img))
                print("IMG is not null")
        data = db.child("Role").get()
        role = data.val()
        var_data.set_relay_val(role)
