import paho.mqtt.client as mqtt
import time

global Connected
Connected = False

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Subscriber connected to MQTT server")
        Connected = True
        client.subscribe("Temperature")
        client.subscribe("Humidity")
        client.subscribe("General")
    else:
        print("Connection failed")

def on_subscribe(client, userdata, message, idk):
    print("Subscribed to: " + str(message) + " " + str(idk))

def on_message(client, userdata, message):
    print("message received: " + str(message.payload))

# MQTT connection
broker_addr = "localhost"
broker_port = 1883
sub_user = "subscriber"
sub_pass = "replace-with-env-pw"

client = mqtt.Client("Temperature-Humidity-Subscriber-1")
client.username_pw_set(username=sub_user, password=sub_pass)

client.on_connect = on_connect
client.on_subscribe = on_subscribe
client.on_message = on_message

client.connect(broker_addr, broker_port, 60)

client.loop_start()

while Connected != True:
    time.sleep(0.1)

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print("Exiting...")
    client.disconnect()
    client.loop_stop()
