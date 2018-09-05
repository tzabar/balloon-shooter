#include <Servo.h>

Servo x_servo;          // create servo object to control a servo
Servo y_servo;          // create servo object to control a servo

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  x_servo.attach(6);    // attaches the servo on pin 9 to the servo object
  y_servo.attach(9);    // attaches the servo on pin 9 to the servo object
  
  Serial.begin(115200);   // begin serial communication at 9600 bits of data per second between the board and the computer

  x_servo.write(90);    // sets the servo position according to the scaled value
  y_servo.write(10);    // sets the servo position according to the scaled value
}

void loop() {
  while (Serial.available() > 0) {
    float x_axis = Serial.parseFloat();   // convert from string to float number
    float y_axis = Serial.parseFloat();   // convert from string to float number
    float detection = Serial.parseFloat();   // convert from string to float number

    if(x_axis > 120)
      x_axis = 120
    else if(x_axis < 60)
      x_axis = 60

    if(y_axis > 60)
      y_axis = 60
    else if(x_axis < 10)
      y_axis = 10
    
    //Serial.print(x_axis);
    //Serial.println(y_axis);

    x_servo.write(x_axis);              // sets the servo position according to the scaled value
    y_servo.write(y_axis);              // sets the servo position according to the scaled value
    if(detection == 0)
      digitalWrite(LED_BUILTIN, LOW);   // turn the LED on (HIGH is the voltage level)
    else
      digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
      
  }
}
