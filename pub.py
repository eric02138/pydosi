import os
import paho.mqtt.client as mqtt
import time
from dotenv import dotenv_values

config = dotenv_values(".env")

BROKER = "localhost"
PORT = 1883
TOPIC = "test/topic"

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect(config.get("BROKER"), int(config.get("PORT")))

topic = f"{config.get("VERSION")}/device"

for i in range(5):
    message = f"Device #{i}"
    result = client.publish(topic, message)
    print(f"Sent: {message}  [status: {result.rc}]")
    time.sleep(1)

client.disconnect()