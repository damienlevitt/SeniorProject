import RPi.GPIO as GPIO


def relay_init(void):
    # Select board pin numbering and check if any pins are mapped twice.
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(True)

    # Using channels 11,13,15 for the positive relay modules.
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)
    GPIO.setup(29, GPIO.OUT)
    GPIO.setup(31, GPIO.OUT)
    GPIO.setup(37, GPIO.OUT)

