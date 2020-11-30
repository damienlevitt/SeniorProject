# Our files
import accelerometer as acc
import level
from IOT import IoT

# Standard libraries
import time
import uuid

if __name__ == "__main__":
    name = "tripod_nick"
    file = open("device_id", "r+")

    device_id = file.read()

    if device_id == "":
        device_id = uuid.uuid4()
        file.write(str(device_id))

    file.close()

    iot = IoT(device_id, name)

    initial_level = acc.is_level()
    iot.pub()

    while True:
        current_level_status = acc.is_level()

        print("LEVEL: " + str(initial_level))
        print("current_level_status: " + str(current_level_status))

        if initial_level != current_level_status:
            iot.pub()
            initial_level = current_level_status

        while iot.auto_level == True:
            try:
                level.level()
            except:
                pass
            time.sleep(1)
        time.sleep(1)