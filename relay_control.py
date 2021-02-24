import RPi.GPIO as io

io.setmode(io.BCM)
powerpin = 23

io.setup(powerpin, io.OUT)
io.output(powerpin, False)


def role(var_data):
    while True:

        _role = var_data.get_relay_val()
        print("role")
        if _role == "1":
            io.output(powerpin, True)
        else:
            io.output(powerpin, False)