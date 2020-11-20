from gpiozero import LED
from time import sleep
import numpy as np

# Value passed is the GPIO pin number.
# Right leg relay module. Value passed is the GPIO pin number.
# relayRU = LED(15)
# relayRD = LED(14)
# # Left leg relay module. Value passed is the GPIO pin number.
# relayLU = LED(24)
# relayLD = LED(23)
# # Middle leg relay module. Value passed is the GPIO pin number.
# relayMU = LED(27)
# relayMD = LED(17)

                            #0,  1,  2,  3,  4,  5
r = np.empty(6, dtype=LED)  #RD, RU, LD, LU, MD, MU,

def extend(relay):
    if relay == 1:
        r[0] = LED(14, initial_value=True)
        r[1] = 0
    if relay == 2:
        r[2] = LED(23, initial_value=True)
        r[3] = 0
    if relay == 3:
        r[4] = LED(17, initial_value=True)
        r[5] = 0
    if relay == 4:
        r[0] = LED(14, initial_value=True)
        r[1] = 0
        r[2] = LED(23, initial_value=True)
        r[3] = 0
        r[4] = LED(17, initial_value=True)
        r[5] = 0
    return


def contract(relay):
    if relay == 1:
        r[0] = 0
        r[1] = LED(15, initial_value=True)
    if relay == 2:
        r[2] = 0
        r[3] = LED(24, initial_value=True)
    if relay == 3:
        r[4] = 0
        r[5] = LED(27, initial_value=True)
    if relay == 4:
        r[0] = 0
        r[1] = LED(15, initial_value=True)
        r[2] = 0
        r[3] = LED(24, initial_value=True)
        r[4] = 0
        r[5] = LED(27, initial_value=True)
    return


def stay(relay):
    if relay == 1:
        r[0] = 0
        r[1] = 0
    if relay == 2:
        r[2] = 0
        r[3] = 0
    if relay == 3:
        r[4] = 0
        r[5] = 0
    if relay == 4:
        r[0] = 0
        r[1] = 0
        r[2] = 0
        r[3] = 0
        r[4] = 0
        r[5] = 0
    return

