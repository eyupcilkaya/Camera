import threading
import camera_control
import database_update
import relay_control
from variables import Variables

cam_data = Variables()

camThread = threading.Thread(target=camera_control.Camera, args=(cam_data,))
dbThread = threading.Thread(target=database_update.Update, args=(cam_data,))
relayThread=threading.Thread(target=relay_control.Role, args=(cam_data,))
camThread.start()
dbThread.start()
relayThread.start()
