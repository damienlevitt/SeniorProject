import accelerometer as acc
import IoT as iot
import level
import linear_driver
import time
import uuid

if __name__ == "__main__":
    device_online = True
    id = uuid.uuid4()
    device_id = str(id)
    power = True
    auto_level = True
    while power:
        iot.publish(device_id, device_online)
        iot.receive()
        iot.disconnect()
        if not acc.is_level() and auto_level is True:
            level.level()
        else:
            pass
        time.sleep(10)




