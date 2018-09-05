import serial

data = serial.Serial('com10', 115200, timeout=1)       # Start the serial port to communicate with arduino

while (True):                                       # infinite while loop to keep the program running
    x_axis = input("Enter x axis: ")                # Prompt the user for x angle
    y_axis = input("Enter y axis: ")                # Prompt the user for y angle
    data.write((x_axis + ',' + y_axis).encode())    # send the angle to the Arduino through serial port
