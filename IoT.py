# Import SDK packages
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
from awscrt import mqtt
import time
import json
import random
import main
import accelerometer as acc
import threading


received_count = 0
received_all_event = threading.Event()

def publish(id, status):
    print("Self-Level-Device is starting...")

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
    print("\nEND PUBLISH\n")

    # Begin Subscribe
    subscribe_future, packet_id = myMQTTClient.subscribe(
        topic="iot/selfLevel-sub",
        QoS=1,
        callback= None)

    subscribe_result = subscribe_future.result()
    print("Subscribed with {}".format(str(subscribe_result['qos'])))

def on_message_received(topic, payload, **kwargs):
    print("Received message from topic '{}': {}".format(topic, payload))
    global received_count
    received_count += 1
    if received_count == 1:
        received_all_event.set()
