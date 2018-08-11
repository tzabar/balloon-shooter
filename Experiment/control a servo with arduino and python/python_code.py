# -*- coding:latin-1 -*-
#import required libraries
import serial
import struct
from vpython import *
import numpy as np
from future.builtins import input

#Start the serial port to communicate with arduino
data = serial.Serial('com5', 9600, timeout=1)

#Create virtual environment:
#first we create the arrow to show current position of the servo
measuringArrow = arrow(pos=vector(0, -10, 0), axis=vector(0, 10, 0), shaftwidth=0.4, headwidth=0.6)
#and the now the labels
angleLabel = label(text='Servo angle is: 90', pos=vector(0, 5, 0), height=15, box=False)
angle0 = label(text='0', pos=vector(-10, -10, 0), height=15, box=False)
angle45 = label(text='45', pos=vector(-7.5, -2.5, 0), height=15, box=False)
angle90 = label(text='90', pos=vector(0, 1, 0), height=15, box=False)
angle135 = label(text='135', pos=vector(7.5, -2.5, 0), height=15, box=False)
angle180 = label(text='180', pos=vector(10, -10, 0), height=15, box=False)

#now we made an infinite while loop to keep the program running
while (True):
    rate(20)  # refresh rate required for VPython
    pos = input("Enter a number: ")  # Prompt the user for the angle
    myLabel = 'Servo angle is: ' + pos  # update the text of the label for the virtual environment
    data.write(pos.encode()) #code and send the angle to the Arduino through serial port
    angleLabel.text = myLabel  # refresh label on virtual environment
    measuringArrow.axis = vector(-10*np.cos(float(pos)*0.01745), 10*np.sin(float(pos)*0.01745), 0)    # calculate the new axis of the indicator