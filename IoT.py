# Import SDK packages
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import time
import json
import random

def publish_status(id, run_event, retry = 5):
    time.sleep(random.randint(1, 3))
    print("Self-Level-Device " + str(id) + " is starting...")

    # Will need to change when updating IoT Core
    IoT_CLIENT = "Self-Leveling-Device" + str(id)
    HOST_NAME = "a2d34x14spudxd-ats.iot.us-west-1.amazonaws.com"
    ROOT_CA = "./AmazonRootCA1.pem"
    PRIVATE_KEY = "./4d62ec6825-private.pem.key"
    CERT_FILE = "./4d62ec6825-certificate.pem.crt"
    myMQTTClient = AWSIoTMQTTClient(IoT_CLIENT)
    myMQTTClient.configureEndpoint(HOST_NAME, 8883)
    myMQTTClient.configureCredentials(ROOT_CA, PRIVATE_KEY, CERT_FILE)
    myMQTTClient.configureOfflinePublishQueueing(-1)
    myMQTTClient.configureDrainingFrequency(2)
    myMQTTClient.configureConnectDisconnectTimeout(10)
    myMQTTClient.configureMQTTOperationTimeout(10)

    connected = False

    while retry != 0 and run_event.is_set():
        try:
            myMQTTClient.connect()
            print("Self-Leveling-Device " + str(id) + " Connected...")
            connected = True
            retry = 0

        except:
            print("Self-Leveling-Device " + str(id) + " failed to connect")

            if (retry != 0):
                retry = retry - 1
                print("Retrying... " + str(retry) + " retries left")
                time.sleep(random.randint(1, 5))
            else:
                print("Out of retries... Exitting")
                return


    if connected == True:

        # Will need to change to match IoT Core
        publish_topic_name = "topic/Self-Leveling-Device"

        random.seed(str(id) + str(time.gmtime()))

        try:
            while run_event.is_set():
                message = {}
                message['id'] = id
                # Change this to accept the status of the Pi
                message['status'] = True if random.randint(0, 1) == 1 else False
                messageJson = json.dumps(message)

                print(messageJson)

                try:
                    myMQTTClient.publish(publish_topic_name, messageJson, 1)
                    time.sleep(random.randint(5, 10))

                except:
                    pass
        except:
            pass

        myMQTTClient.disconnect()

    print("Exitting...")

    return