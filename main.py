import threading
import camera_control
import database_update
from variables import Variables

cam_data = Variables()

camThread = threading.Thread(target=camera_control.Camera, args=(cam_data,))
dbThread = threading.Thread(target=database_update.upload, args=(cam_data,))

camThread.start()
dbThread.start()
