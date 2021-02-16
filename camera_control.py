from datetime import datetime
import cv2
import variables
import os

cap = cv2.VideoCapture(0)

def Camera(var_data):
    a = datetime.now()

    if not os.path.exists('pictures'):
        os.makedirs('pictures')

    while (True):
        b=datetime.now()
        ret, frame = cap.read()
        if (b - a).microseconds >= 500000 :
            a = b
            img="pictures/{}.jpg".format(1)
            cv2.imwrite(f"{img}", frame, [cv2.IMWRITE_JPEG_QUALITY, 50])
            var_data.set_cam_data(img)
