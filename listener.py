import os
import paho.mqtt.client as mqtt
from dotenv import dotenv_values

config = dotenv_values(".env")

topic = f"{config.get("VERSION")}/device"

def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected with code: {reason_code}")
    client.subscribe(topic)

def on_message(client, userdata, msg):
    print(f"Received: [{msg.topic}] {msg.payload.decode()}")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message

client.connect(config.get("BROKER"), int(config.get("PORT")))
client.loop_forever()