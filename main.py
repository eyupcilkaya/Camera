import threading
import camera_control
import database_update
import relay_control
from variables import Variables

cam_data = Variables()

camThread = threading.Thread(target=camera_control.camera, args=(cam_data,))
dbThread = threading.Thread(target=database_update.update, args=(cam_data,))
relayThread = threading.Thread(target=relay_control.role, args=(cam_data,))

camThread.start()
dbThread.start()
relayThread.start()
