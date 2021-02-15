import threading
import camera_control
import database_update

camThread = threading.Thread(target=camera_control.Camera)
dbThread = threading.Thread(target=database_update.upload)

camThread.start()
dbThread.start()
