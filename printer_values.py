import serial
import pandas as pd

serialcon = serial.Serial(port="COM5",
                          baudrate=115200,
                          parity=serial.PARITY_NONE,
                          stopbits=serial.STOPBITS_ONE,
                          bytesize=serial.EIGHTBITS,
                          timeout=1)

while 1:
    x = serialcon.readline().decode('utf-8').rstrip()
    if x[0:17] == "SD printing byte ":
        print(x[17:], "Done!")

    line = x.split(" ")
    v = pd.Series(line)

    if v.size > 3:
        for i in v:
            if i[0:2] in "T:":
                print("Nozzle Temp:", i[2:])
            elif i[0:2] in "B:":
                print("Base Temp:", i[2:])
            else:
                continue
