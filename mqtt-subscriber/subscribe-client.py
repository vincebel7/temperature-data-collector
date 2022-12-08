"""
mqtt-subscriber.py
Author: vincebel7
Purpose: Subscribes to the MQTT server and redirects messages to other services, such as Redis
"""

import paho.mqtt.client as mqtt
import time
import redis
import json

global Connected
Connected = False

def on_connect(mqtt_client, userdata, flags, rc):
    if rc == 0:
        print("Subscriber connected to MQTT server")
        Connected = True
        mqtt_client.subscribe("General")
    else:
        print("Connection failed")

def on_subscribe(mqtt_client, userdata, message, idk):
    print("Subscribed to MQTT server")

def on_message(mqtt_client, userdata, message_str):
    payload = message_str.payload.decode('utf8')
    jsonload = json.loads(payload)
    jsondump = json.dumps(jsonload)
    
    print("Data received: " + jsondump)

    # Add to Redis
    redis_client.publish("DHT-data", str(jsondump))

# Redis connection
redis_host = "localhost"
redis_port = 6379
redis_db = 0

redis_client = redis.StrictRedis(redis_host, redis_port, redis_db)
redis_channel = "DHT-data"

# MQTT connection
broker_addr = "localhost"
broker_port = 1883
sub_user = "subscriber"
sub_pass = "replace-with-env-pw"

mqtt_client = mqtt.Client("Temperature-Humidity-Subscriber-1")
mqtt_client.username_pw_set(username=sub_user, password=sub_pass)

mqtt_client.on_connect = on_connect
mqtt_client.on_subscribe = on_subscribe
mqtt_client.on_message = on_message

mqtt_client.connect(broker_addr, broker_port, 60)

mqtt_client.loop_start()

while Connected != True:
    time.sleep(0.1)

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print("Exiting...")
    mqtt_client.disconnect()
    mqtt_client.loop_stop()
