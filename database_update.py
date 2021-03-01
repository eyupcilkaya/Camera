from _datetime import datetime
from pyrebase import pyrebase
import firebaseConfigFile

firebase = pyrebase.initialize_app(firebaseConfigFile.firebaseConfig)
storage = firebase.storage()
db = firebase.database()


def update(var_data):
    a = datetime.now()

    while True:
        t1, t2, p = var_data.get_sensor_val()
        b = datetime.now()
        if (b - a).seconds >= 1:
            a = b
            img = var_data.get_cam_data()

            if img != "":
                storage.child("1.jpg").put("{}".format(img))
                print("IMG is not null")

        db.child("Base Temp").set(t1)
        db.child("Nozzle Temp").set(t2)
        db.child("Process").set(p)

        data = db.child("Relay").get()
        relay = data.val()
        var_data.set_relay_val(relay)
