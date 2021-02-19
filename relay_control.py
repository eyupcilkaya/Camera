import RPi.GPIO as io

io.setmode(io.BCM)
powerpin = 23

io.setup(powerpin, io.OUT)
io.output(powerpin, False)

def Role(var_data):
    while (True):

        role = var_data.get_relay_val()
        print("role")
        if role == "1":
            io.output(powerpin, True)
        else:
            io.output(powerpin, False)