from datetime import datetime
import cv2
import os

cap = cv2.VideoCapture(0)

def Camera(var_data):
    a = datetime.now()

    if not os.path.exists('pictures'):
        os.makedirs('pictures')
    i = 0
    while (True):

        ret, frame = cap.read()
        if i < 10:
            b = datetime.now()
            if (b - a).microseconds >= 500000 :
                a = b
                img="pictures/{}.jpg".format(i)
                cv2.imwrite(f"{img}", frame, [cv2.IMWRITE_JPEG_QUALITY, 50])
                var_data.set_cam_data(img)
                i=i+1
        else:
            i=0
