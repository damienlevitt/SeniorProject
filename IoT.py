# Import SDK packages
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import time
import json
import random
import accelerometer as acc
from threading import Event


def publish_status(id, run_event, retry = 5):
    time.sleep(random.randint(1, 3))
    print("Self-Level-Device " + str(id) + " is starting...")

    # Will need to change when updating IoT Core
    IoT_CLIENT = "Self-Leveling-Device" + str(id)
    HOST_NAME = "a2d34x14spudxd-ats.iot.us-west-1.amazonaws.com"
    ROOT_CA = "certs/AmazonRootCA1.pem"
    PRIVATE_KEY = "certs/4d62ec6825-private.pem.key"
    CERT_FILE = "certs/4d62ec6825-certificate.pem.crt"
    myMQTTClient = AWSIoTMQTTClient.AWSIoTMQTTClient(IoT_CLIENT)
    myMQTTClient.configureEndpoint(HOST_NAME, 8883)
    myMQTTClient.configureCredentials(ROOT_CA, PRIVATE_KEY, CERT_FILE)
    myMQTTClient.connect()
    print("connected")
    for i in range(5):
        print("in loop")
        AWSIoTMQTTClient.publish("iot/selfLevel", acc.is_level(), 1)
        print("Published: level status to the topic: " + "'iot/selfLevel'")
        time.sleep(2)

    print("End publish")

    AWSIoTMQTTClient.disconnect()