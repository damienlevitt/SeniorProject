import linear_driver as ld
import accelerometer as acc
from time import sleep
import numpy as np

# M Being low makes x positive
# R Being low makes y negative
# L Being low makes y positive
wait_time = 0.1
level_state = 0.3
acc_due_to_motors = 0.2


def leveler():
    x, y, z = acc.value()
    if y < level_state:
        while y < level_state:
            ld.extend(1)
            sleep(wait_time)
            x, y, z = acc.value()
        ld.stay(1)
    else:
        while y > level_state:
            ld.extend(2)
            sleep(wait_time)
            x, y, z = acc.value()
        ld.stay(2)
    sleep(wait_time)
    x, y, z = acc.value()
    print(acc.value())
    if x > level_state:
        while x > (level_state - acc_due_to_motors):
            ld.extend(3)
            sleep(wait_time)
            x, y, z = acc.value()
        ld.stay(3)
    else:
        while x < (level_state + acc_due_to_motors):
            ld.extend(1)
            ld.extend(2)
            sleep(wait_time)
            x, y, z = acc.value()
        ld.stay(4)
    sleep(wait_time*5)
    x, y, z = acc.value()
    print(acc.value())
    return acc.is_level()


def level():
    done = 0
    while not done:
        done = leveler()
        print(done)


level()
