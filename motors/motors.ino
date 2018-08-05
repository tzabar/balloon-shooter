#include <Servo.h>

Servo x_servo;          // create servo object to control a servo
Servo y_servo;          // create servo object to control a servo

void setup() {
  x_servo.attach(6);    // attaches the servo on pin 9 to the servo object
  y_servo.attach(9);    // attaches the servo on pin 9 to the servo object
  
  Serial.begin(9600);   // begin serial communication at 9600 bits of data per second between the board and the computer

  x_servo.write(90);    // sets the servo position according to the scaled value
  y_servo.write(10);    // sets the servo position according to the scaled value
}

void loop() {
  while (Serial.available() > 0) {
    int x_axis = Serial.parseFloat();   // convert from string to float number
    int y_axis = Serial.parseFloat();   // convert from string to float number
    
    Serial.print(x_axis);
    Serial.println(y_axis);

    x_servo.write(x_axis);              // sets the servo position according to the scaled value
    y_servo.write(y_axis);              // sets the servo position according to the scaled value
  }
}