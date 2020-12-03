# SeniorProject
## Self Leveling IOT Device
This repo includes the drivers for the linear actuators, and the accelerometer, and a main program that receives commands from aws and sends the level status.

## Software Setup
* Install the following libraries on the Raspberry Pi
    * adafruit_adxl34x
    * gpioZero
    * AWSIoTPythonSDK.MQTTLib
* Copy all of the python files to one directory on the Raspberry Pi 
##Hardware Setup
* Enable I2c and the raspberry Pi
* Connect relays
    * GPIO pin 14
    * GPIO pin 15
    * GPIO pin 23
    * GPIO pin 24
    * GPIO pin 17
    * GPIO pin 27
* Accelerometer
    * GPIO pin 2 (SDA)
    * GPIO pin 3 (SCL)
* Remember to make all source and ground connections for the accelerometer and relays.
