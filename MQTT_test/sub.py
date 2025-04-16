import paho.mqtt.client as mqtt

# broker = "broker.hivemq.com"
broker = "test.mosquitto.org"
topic = "cricket/live_score129"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker! Subscribing...")
        client.subscribe(topic)
    else:
        print(f"Failed to connect, return code {rc}")

def on_message(client, userdata, msg):
    print(f"Received: {msg.payload.decode()} on {msg.topic}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker, 1883, 60)
client.loop_forever()
