"""
mqtt-subscriber.py
Author: vincebel7
Purpose: Subscribes to the MQTT server and redirects messages to other services, such as Redis
"""

import paho.mqtt.client as mqtt
import time
import redis
import json
import os
import pathlib
import sqlalchemy as db
from dotenv import load_dotenv

file_path = pathlib.Path(__file__).parent.resolve()
load_dotenv(str(file_path) + '/../.env')

USE_MYSQL = os.getenv("USE_MYSQL") # True / False
MYSQL_HOST = str(os.getenv("DB_HOST"))
MYSQL_DB = str(os.getenv("DB_NAME"))
MYSQL_USER = str(os.getenv("DB_USER"))
MYSQL_PASS = str(os.getenv("DB_PASS"))
MYSQL_PORT = 3306

MQTT_BROKER = "localhost"
MQTT_SUB_USER = os.getenv("MQTT_SUB_USER")
MQTT_SUB_PASS = os.getenv("MQTT_SUB_PASS")
MQTT_PORT = 1883

REDIS_HOST = "localhost"
REDIS_DB = 0
REDIS_CHANNEL = "DHT-data"
REDIS_PORT = 6379

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
    redis_client.publish(REDIS_CHANNEL, str(jsondump))

    if(USE_MYSQL == True): insert_mysql(mqtt_client, jsondump)

def insert_mysql(mqtt_client, message):
    return

# MySQL connection
if(USE_MYSQL == True):
    print("Connecting to MySQL...")
    mysql_conn_string = "mysql://" + MYSQL_USER + ":" + MYSQL_PASS + "@" + MYSQL_HOST + ":" + str(MYSQL_PORT) + "/" + MYSQL_DB
    engine = db.create_engine(mysql_conn_string)
    conn = engine.connect()

# Redis connection
redis_host = "localhost"
redis_port = 6379
redis_db = 0

redis_client = redis.StrictRedis(redis_host, redis_port, redis_db)

# MQTT connection
mqtt_client = mqtt.Client("Temperature-Humidity-Subscriber-1")
mqtt_client.username_pw_set(username=MQTT_SUB_USER, password=MQTT_SUB_PASS)

mqtt_client.on_connect = on_connect
mqtt_client.on_subscribe = on_subscribe
mqtt_client.on_message = on_message

mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)

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
