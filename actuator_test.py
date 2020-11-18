import linear_init as linear
import time

# Test the left leg up.
linear.relayLU.on()
time.sleep(2)
linear.relayLU.off()

# Test the left leg down.
linear.relayLD.on()
time.sleep(2)
linear.relayLD.off()

# Test the right leg up.
linear.relayRU.on()
time.sleep(2)
linear.relayRU.off()

# Test the right leg down.
linear.relayRD.on()
time.sleep(2)
linear.relayRD.off()

# Test the middle leg up.
linear.relayMU.on()
time.sleep(2)
linear.relayMD.off()

# Test the middle leg down.
linear.relayMD.on()
time.sleep(2)
linear.relayMD.off()
