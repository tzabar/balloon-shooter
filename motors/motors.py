import serial


class motors():
    def __init__(self):
        # Start the serial port to communicate with arduino
        data = serial.Serial('com10', 115200, timeout=1)

    def move_laser(x_axis, y_axis, detection):
        # send the angle to the Arduino through serial port
        data.write((x_axis + ',' + y_axis + ',' + detection).encode())
