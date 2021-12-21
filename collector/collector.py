import dht
import time
from pyA20.gpio import gpio
from pyA20.gpio import port

#initialize GPIO
PIN2 = port.PA6
gpio.init()

#instance = dht.DHTSensor(pin=PIN2, sensor="DHT11")
instance = dht.DHTSensor(pin=PIN2, sensor="DHT22")

# read data using pin port.PA6
def read_sensor():
    response = instance.read_pin()

    if response.error_code == 0:
        print("Temp: " + str(response.temperature))
        print("Humidity: " + str(response.humidity))
    # MQTT send here
    else:
        print("Error: %d" % response.error_code)

while True:
    read_sensor()
    time.sleep(0.5)
