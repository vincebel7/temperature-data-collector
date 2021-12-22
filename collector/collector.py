import dht
import time
import paho.mqtt.client as mqtt
from pyA20.gpio import gpio
from pyA20.gpio import port

#initialize GPIO
PIN = port.PA6
gpio.init()

#instance = dht.DHTSensor(pin=PIN2, sensor="DHT11")
instance = dht.DHTSensor(pin=PIN, sensor="DHT22")

mqttIP = "192.168.5.235"
client = mqtt.Client("Temperature-Humidity")
client.connect(mqttIP, 1883, 60)

# read data using pin port.PA6
def read_sensor():
    response = instance.read_pin()

    if response.error_code == 0:
        print("Temp: " + str(response.temperature))
        print("Humidity: " + str(response.humidity))
        client.publish("Temperature", str(response.temperature))
        client.publish("Humidity", str(response.humidity))
    else:
        print("Error: %d" % response.error_code)

while True:
    read_sensor()
    time.sleep(0.5)
