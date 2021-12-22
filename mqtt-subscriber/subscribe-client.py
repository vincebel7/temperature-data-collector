import paho.mqtt.client as mqtt

mqttIP = "localhost"
client = mqtt.Client("Temperature-Humidity")

def on_message(client, userdata, message):
    time.sleep(1)
    print("received message =",str(message.payload.decode("utf-8")))

client.connect(mqttIP, 1883, 60)

client.subscribe("Temperature")
client.on_message=on_message

client.loop_forever()
