# Import SDK packages
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import time
import json
import random
import main
import accelerometer as acc
from threading import Event


def publish_status(id, status, retry = 5):
    print("Self-Level-Device " + str(id) + " is starting...")

    # Will need to change when updating IoT Core
    IoT_CLIENT = "tripod_damien"
    HOST_NAME = "a2d34x14spudxd-ats.iot.us-west-1.amazonaws.com"
    ROOT_CA = "certs/AmazonRootCA1.pem"
    PRIVATE_KEY = "certs/4d62ec6825-private.pem.key"
    CERT_FILE = "certs/4d62ec6825-certificate.pem.crt"
    myMQTTClient = AWSIoTMQTTClient(IoT_CLIENT)
    myMQTTClient.configureEndpoint(HOST_NAME, 8883)
    myMQTTClient.configureCredentials(ROOT_CA, PRIVATE_KEY, CERT_FILE)
    myMQTTClient.configureOfflinePublishQueueing(-1)
    myMQTTClient.configureDrainingFrequency(2)
    myMQTTClient.configureConnectDisconnectTimeout(10)
    myMQTTClient.configureMQTTOperationTimeout(10)
    myMQTTClient.connect()

    # AWS Message Contents
    print("\n-----------------------------------------\n")
    print("CONNECTION MADE!\n")
    message = {}
    message['id'] = id
    message['level'] = acc.is_level()
    message['battery'] = "100"
    message['healthy'] = status
    messageJson = json.dumps(message)
    myMQTTClient.publish("iot/selfLevel", messageJson, 1)

    # Console Message
    print("PUBLISHED: Status to topic: 'iot/selfLevel'\n")
    print("Device ID: ", id)
    print("Level: ", acc.is_level())
    print("Battery: 100")
    print("Healthy: ", status)
    time.sleep(2)
    print("\nEND PUBLISH -- DISCONNECTING\n")
    myMQTTClient.disconnect()