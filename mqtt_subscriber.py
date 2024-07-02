import sys
import paho.mqtt.client as ph

def message_handling(client, userdata, msg):
    print(f"{msg.topic}: {msg.payload.decode()}")

client = ph.Client()
client.on_message = message_handling

if client.connect("localhost", 1883, 60) != 0:
    print("Couldn't connect to the MQTT broker")
    sys.exit(1)

client.subscribe("test_topic")

try:
    print("Press CTRL+C to exit...")
    client.loop_forever()
except KeyboardInterrupt:
    print("Caught an Exception, something went wrong...")
finally:
    print("Disconnecting from the MQTT broker")
    client.disconnect()
