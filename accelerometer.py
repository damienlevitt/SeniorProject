import time
import board
import busio
import adafruit_adxl34x
import numpy as np

i2c = busio.I2C(board.SCL, board.SDA)
accelerometer = adafruit_adxl34x.ADXL345(i2c)


def value():
    return accelerometer.acceleration


def abs_value():
    x, y, z = accelerometer.acceleration
    return np.sqrt(np.power(x-0.3, 2)+np.power(y-0.3, 2)+np.power(z-9.8, 2))


def is_level():
    if abs_value() < 1.4 and abs_value() > 1.2:
        return True
    else:
        return False


print(value())
print(abs_value())
print(is_level())
