import paho.mqtt.client as mqtt
import time

BROKER = "localhost"
PORT = 1883
TOPIC = "test/topic"

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect(BROKER, PORT)

for i in range(5):
    message = f"Hello MQTT #{i}"
    result = client.publish(TOPIC, message)
    print(f"Sent: {message}  [status: {result.rc}]")
    time.sleep(1)

client.disconnect()