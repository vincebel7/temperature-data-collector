import dht
import time
import redis
from pyA20.gpio import gpio
from pyA20.gpio import port

#initialize GPIO
PIN2 = port.PA6
gpio.init()

instance = dht.DHTSensor(pin=PIN2)

def insert_redis(result):
    print("Adding to redis...")

#read data using pin port.PA6
def read_sensor():
    response = instance.read_pin()

    #print(response.temperature)
    if response.error_code == 0:
        #print("Temperature: %.2f" % response.temperature)
        print("Temp: " + str(response.temperature))
        print("Humidity: " + str(response.humidity))
   #     insert_redis(result)
    else:
        print("Error: %d" % response.error_code)

while True:
    read_sensor()
    time.sleep(0.5)
