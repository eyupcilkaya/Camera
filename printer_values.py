from datetime import datetime

import serial
import pandas as pd

serialcon = serial.Serial(port="COM4",
                          baudrate=115200,
                          parity=serial.PARITY_NONE,
                          stopbits=serial.STOPBITS_ONE,
                          bytesize=serial.EIGHTBITS,
                          timeout=1)
a=datetime.now()
while 1:

    b = datetime.now()
    if (b - a).seconds >= 10:
        serialcon.write(b'M05')
        a = b

    x = serialcon.readline().decode('utf-8').rstrip()
    print(x)
    if x[0:17] == "SD printing byte ":
        print(x[17:], "Done!")
        continue

    line = x.split(" ")
    v = pd.Series(line)

    if v.size > 3:
        for i in v:
            if i[0:2] == "T:":
                print("Nozzle Temp:", i[2:])
            elif i[0:2] == "B:":
                print("Base Temp:", i[2:])
            else:
                continue
