import sys
import paho.mqtt.client as paho

client = paho.Client()

if client.connect("localhost", 1883, 60) != 0:
    print("couldn't connect to the mqtt broker !")
    sys.exit()

client.publish("test_topic", "Hi , paho client works fine: ", 0)
client.disconnect()
