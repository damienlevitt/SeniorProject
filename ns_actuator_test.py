import linear_driver as ld
import time

# Right leg
ld.extend(1)
time.sleep(2)
ld.stay(1)
time.sleep(2)
ld.contract(1)
time.sleep(2)
ld.stay(1)

#wait
time.sleep(2)

# Left Leg
ld.extend(2)
time.sleep(2)
ld.stay(2)
time.sleep(2)
ld.contract(2)
time.sleep(2)
ld.stay(2)

#wait
time.sleep(2)

# Middle Leg
ld.extend(3)
time.sleep(2)
ld.stay(3)
time.sleep(2)
ld.contract(3)
time.sleep(2)
ld.stay(3)

#wait
time.sleep(2)

# All Legs
ld.extend(4)
time.sleep(2)
ld.stay(4)
time.sleep(2)
ld.contract(4)
time.sleep(2)
ld.stay(4)
