import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(channel, GPIO.out)


def motor_on(pin):
    GPIO.output(pin, GPIO.HIGH)


def motor_off(pin):
    GPIO.output(pin, GPIO.LOW)



