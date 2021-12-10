# Read values off GPIO pins

import time
from pyA20.gpio import gpio, port

class DHTResponse:
        temperature = -1
        humidity = -1

        def __init__(self, temperature, humidity):
            self.temperature = temperature
            self.humnidity = humidity

class DHTSensor:
    __pin = -1

    def __init__(self, pin):
        self.__pin = pin

    def read_pin(self):
        gpio.output(gpio.HIGH)
        time.sleep(0.05) # 50 msec

        gpio.output(gpio.LOW)
        time.sleep(0.02) # 20 msec

        raw_input = self.__input_listen()

        response = DHTResponse(raw_input, 0)
        return(response)

    def __input_listen(self):
        # input
        prev = -1
        repeat_counter = 0
        data = []
        bits_to_read = True

        while bits_to_read:
            input = gpio.input(self.__pin)
            data.append(input)

            if input == prev:
                repeat_counter += 1
                if repeat_counter > 50:
                    bits_to_read = False
            else:
                repeat_counter = 0

            prev = input

        return data
