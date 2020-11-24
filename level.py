import linear_driver as ld
import accelerometer as acc
from time import sleep
import numpy as np

# M Being low makes x positive
# R Being low makes y negative
# L Being low makes y positive
wait_time = 0.3
level_state_x = 0.19
level_state_y = 0.15
acc_due_to_motors = 0.0


def leveler():
    x, y, z = acc.value()
    if y < level_state_y:
        while y < level_state_y:
            ld.extend(1)
            sleep(wait_time)
            x, y, z = acc.value()
        ld.stay(1)
    else:
        while y > level_state_y:
            ld.extend(2)
            sleep(wait_time)
            x, y, z = acc.value()
        ld.stay(2)
    sleep(wait_time)
    x, y, z = acc.value()
    print(acc.value())
    if x > level_state_x:
        while x > level_state_x:
            ld.extend(3)
            sleep(wait_time)
            x, y, z = acc.value()
        ld.stay(3)
    else:
        while x < (level_state_x + acc_due_to_motors):
            ld.extend(1)
            ld.extend(2)
            sleep(wait_time)
            x, y, z = acc.value()
        ld.stay(4)
    sleep(wait_time*10)
    x, y, z = acc.value()
    print(acc.value())
    return acc.is_level()


def level():
    done = (0, 1)[acc.is_level()]
    while not done:
        done = leveler()
        print(done)
