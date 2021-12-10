# Library to read values off GPIO pins
import time
from pyA20.gpio import gpio, port

class DHT:
    __pin = -1

    def __init__(self, pin):
        self.__pin = pin

    def read_pin(self):
        iput = gpio.input(self.__pin)
        print(iput)
