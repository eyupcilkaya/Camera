
import serial
import pandas as pd
serialcon=serial.Serial(port="serial_port",baudrate=115200,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=1)
while 1:
    x=serialcon.readline().decode('utf-8').rstrip()
    print(x)
    if x[0:17] == "SD printing byte ":
        print(x[17:],"tamamlandi")
    line=x.split(" ")
    v=pd.Series(line)
    for i in v:
        if i[0:2] in "T:":
            print("T SICAKLIK:",i[2:])

        elif i[0:2] in "B:":
            print("B SICAKLIK:",i[2:])
        else:
            continue