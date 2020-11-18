from gpiozero import LED
from time import sleep

# Value passed is the GPIO pin number.
# Left leg relay module. Value passed is the GPIO pin number.
relayLU = LED(24, initial_value=False)
relayLD = LED(23, initial_value=False)

# Right leg relay module. Value passed is the GPIO pin number.
relayRU = LED(15, initial_value=False)
relayRD = LED(14, initial_value=False)

# Middle leg relay module. Value passed is the GPIO pin number.
relayMU = LED(27, initial_value=False)
relayMD = LED(17, initial_value=False)



