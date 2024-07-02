import sys
import paho.mqtt.client as ph
import json
import time

client = ph.Client()

if client.connect("localhost", 1883, 60) != 0:
    print("couldn't connect to the mqtt broker !")
    sys.exit()

with open('data.json', 'r') as f:
    orders = json.load(f)

def publish_order():
    for order in orders:
        name = order['customerName']
        orderNumber = order['orderNumber']
        client.publish("order_topic",f"name = \"{name}\" and order_number = \"{orderNumber}\"" , 0) 
        time.sleep(3)
    client.disconnect()

publish_order()