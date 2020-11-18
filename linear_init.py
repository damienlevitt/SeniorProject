from gpiozero import LED
from time import sleep

# Value passed is the GPIO pin number.
# Left leg relay module. Value passed is the GPIO pin number.
relayLU = LED(24)
relayLD = LED(23)

# Right leg relay module
relayRU = LED(15)
relayRD = LED(14)

# Middle leg relay module
relayMU = LED(27)
relayMD = LED(17)



