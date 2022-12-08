import dht
import time
import datetime
import json
import paho.mqtt.client as mqtt
from pyA20.gpio import gpio
from pyA20.gpio import port

#initialize GPIO
PIN = port.PA6
gpio.init()

#instance = dht.DHTSensor(pin=PIN2, sensor="DHT11")
instance = dht.DHTSensor(pin=PIN, sensor="DHT22")

mqttIP = "192.168.5.235"
#mqttIP = "localhost"
client = mqtt.Client("Temperature-Humidity-Publisher-1")
client.username_pw_set(username="publisher", password="replace-with-env-pw")
client.connect(mqttIP, 1883, 60)

def build_message(response):
    temperature = str(response.temperature)
    humidity = str(response.humidity)
    time = datetime.datetime.now().isoformat()

    # dictionary
    msg = {
        "time": time,
        "temperature": temperature,
        "humidity": humidity,
    }

    return msg

# read data using pin port.PA6
def read_sensor():
    response = instance.read_pin()

    if response.error_code == 0:
        msg = build_message(response)
        print("Temperature: " + msg.get("temperature"))
        print("Humidity: " + msg.get("humidity"))

        # Can't publish dict, so convert to string and convert back on subscriber
        stringed_msg = str(json.dumps(msg))
        print(stringed_msg)
        client.publish("General", stringed_msg)
    else:
        print("Error: %d" % response.error_code)

while True:
    read_sensor()
    time.sleep(0.5)
