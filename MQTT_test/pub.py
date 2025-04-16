import paho.mqtt.client as mqtt
from test_cricbuzz import get_live_score
import time

# broker = "broker.hivemq.com"
broker = "test.mosquitto.org"
topic = "cricket/live_score129"

client = mqtt.Client()

while True:
    client.connect(broker, 1883, 60)

    score = get_live_score()
    result = client.publish(topic, score, retain=True)

    # Check if the message was successfully sent
    if result.rc == 0:
        print(f"Published successfully: {score}")
    else:
        print("Failed to publish message")

    client.disconnect()
    time.sleep(60)
