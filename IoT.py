# Our files
import accelerometer as acc
import level

# Standard libraries
import json

# Third party libraries
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

HOST_NAME = "a2d34x14spudxd-ats.iot.us-west-1.amazonaws.com"
ROOT_CA = "certs/AmazonRootCA1.pem"
PRIVATE_KEY = "certs/a46c3aefe0-private.pem.key"
CERT_FILE = "certs/a46c3aefe0-certificate.pem.crt"


class IoT:
    id = None
    name = None
    auto_level = False
    connection = None

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.connection = self.get_connection()
        self.sub()

    def get_connection(self):
        if self.name == None or self.id == None:
            return None

        connection = AWSIoTMQTTClient(self.name)
        connection.configureEndpoint(HOST_NAME, 8883)
        connection.configureCredentials(ROOT_CA, PRIVATE_KEY, CERT_FILE)
        connection.configureOfflinePublishQueueing(-1)
        connection.configureDrainingFrequency(2)
        connection.configureConnectDisconnectTimeout(10)
        connection.configureMQTTOperationTimeout(10)
        connection.connect()
        return connection

    def pub(self, message = None):
        message = {}
        message['id'] = self.id
        message['level'] = acc.is_level()
        message['battery'] = "100"
        message['healthy'] = True

        try:
            print("Publishing status to AWS...")
            self.connection.publish("iot/selfLevel", json.dumps(message), 1)
            print("Publish Completed")
        except:
            print("Could not publish to the AWS server!")

    def sub(self):
        print("Subscribing to topic command...")
        self.connection.subscribe(topic = "command", QoS = 1, callback = self.sub_callback)
        print("Subscribed to topic command")

    def sub_callback(self, client, userdata, message):
        payload = json.loads(message.payload.decode().replace("'", '"'))

        if payload["id"] != self.id:
            return

        command = payload["command"]
        print(command)

        if command == "AUTO_LEVEL_ON":
            self.auto_level = True
        elif command == "AUTO_LEVEL_OFF":
            self.auto_level = False
        elif command == "LEVEL":
            level.level()

