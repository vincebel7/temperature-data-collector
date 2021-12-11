# Read values off GPIO pins
# I still have a fuzzy understanding of this, this was a lot of trial + error
# Special thanks to the many others who have provided similar libraries and 
# step-by-step tutorials on parsing signals off the GPIO pins.

import time
from pyA20.gpio import gpio, port

class DHTResponse:
        temperature = -1
        humidity = -1
        error_code = -1

        def __init__(self, temperature, humidity, error_code):
            self.temperature = temperature
            self.humnidity = humidity
            self.error_code = error_code

        def __get_error_code(self):
            return self.error_code

        def get_error_text(code):
            if code == 0:
                return "Success"
            if code == 1:
                return "No data"
            if code == 2:
                return "Bad data"
            if code == 3:
                return ""

class DHTSensor:
    __pin = -1

    def __init__(self, pin):
        self.__pin = pin

    def read_pin(self):

        # switch to putput for high/low
        gpio.setcfg(self.__pin, gpio.OUTPUT)

        gpio.output(self.__pin, 1)
        time.sleep(0.03) # 50 msec

        gpio.output(self.__pin, 0)
        time.sleep(0.03) # 20 msec

        # switch to input for listening
        gpio.setcfg(self.__pin, gpio.INPUT)

        raw_input = self.__input_listen()
        
        # Get period lengths
        # 1-8: Humidity (integer)
        # 9-16: Humidity (decimal)
        # 17-24: Temperature (integer)
        # 25-32: Temperature (decimal)
        # 33-40: Checksum
        period_lengths = self.__get_period_lengths(raw_input)
        
        # Period length validation
        if len(period_lengths) == 0:
            response = DHTResponse(0, 0, 1)
            print(DHTResponse.get_error_text(response.error_code))
            return(response)

        elif len(period_lengths) != 40:
            response = DHTResponse(0, 0, 2)
            print(DHTResponse.get_error_text(response.error_code))
            return(response)

        print(period_lengths)

        bits = self.__convert_to_bits(period_lengths)
        
        response = DHTResponse(bits, 0, 0)
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

    def __get_period_lengths(self, data):
        periods = []
        payload_len = 0
        step = 1 # init down, init up, data down, data up, data down

        for i in range(len(data)):
            val = data[i]
            payload_len += 1

            if step == 1 and val == 0: # init low
                step = 2

            if step == 2 and val == 1: # init high
                step = 3

            if step == 3 and val == 0: # data down
                step = 4

            if step == 4 and val == 1: # data up
                payload_len = 0
                step = 5

            if step == 5 and val == 0: # data down, we are receiving payload
                periods.append(payload_len)
                step = 4

        return periods

    def __convert_to_bits(self, data):
        bits = []

        # TODO: Use lengths of periods to calculate 0 or 1

        return bits
