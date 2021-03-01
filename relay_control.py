import RPi.GPIO as io

io.setmode(io.BCM)
powerpin = 23

io.setup(powerpin, io.OUT)
io.output(powerpin, False)


def relay(var_data):
    while True:

        _relay = var_data.get_relay_val()
        if _relay == "1":
            io.output(powerpin, True)
        else:
            io.output(powerpin, False)