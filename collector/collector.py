import dht
import time
import redis
from pyA20.gpio import gpio
from pyA20.gpio import port

#initialize GPIO
PIN2 = port.PA6
gpio.init()

def insert_redis(result):
    print("Adding to redis...")

#read data using pin port.PA6
def read_sensor():
    instance = dht.DHT(pin=PIN2)
    response = instance.read_pin()
    print(response.temperature)
    #print(str(result.temperature) + " " + str(result.humidity))
   # if result.is_valid():
   #     print("Temperature: %.2f" % result.temperature)
   #     print("Humidity: %.2f" % result.humidity)
   #     insert_redis(result)
    #else:
    #    print("Error: %d" % result.error_code)

while True:
    read_sensor()
    time.sleep(0.2)
