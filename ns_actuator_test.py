import linear_driver as ld
import time

# Test the left leg up.
ld.extend(1)
time.sleep(2)
ld.contract(1)

# Test the left leg down.
ld.extend(2)
time.sleep(2)
ld.contract(2)

# Test the right leg up.
ld.extend(3)
time.sleep(2)
ld.contract(3)

# Test the right leg down.
ld.extend(4)
time.sleep(2)
ld.contract(4)
