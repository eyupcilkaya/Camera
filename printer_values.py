from datetime import datetime

import serial
import pandas as pd

serialcon = serial.Serial(port="COM4",
                          baudrate=115200,
                          parity=serial.PARITY_NONE,
                          stopbits=serial.STOPBITS_ONE,
                          bytesize=serial.EIGHTBITS,
                          timeout=1)


def printer_val(var_data):
    a = datetime.now()
    p = 0
    t1 = 0
    t2 = 0

    while 1:
        b = datetime.now()
        if (b - a).seconds >= 5:
            serialcon.write(b'M05')
            a = b
        x = serialcon.readline().decode('utf-8').rstrip()
        if x[0:17] == "SD printing byte ":
            g = x[17:]
            g = g.split("/")
            p = int((int(g[0]) / int(g[1])) * 100)
            print(x[17:], "Done!")
            continue

        line = x.split(" ")
        v = pd.Series(line)

        if v.size > 3:
            for i in v:
                if i[0:2] == "T:":
                    t1 = i[2:]
                    print("Nozzle Temp:", i[2:])
                elif i[0:2] == "B:":
                    t2 = i[2:]
                    print("Base Temp:", i[2:])
                else:
                    continue
        var_data.set_sensor_val(t1, t2, p)
