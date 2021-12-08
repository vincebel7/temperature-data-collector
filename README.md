# DHT-display-server
An application to log and display humidity and temperature data from a digital temperature and humidity sensor (DHT)

Currently pulling pre-inserted test data from a MySQL database, until I get the Arduino component working. Need to acquire a new Arduino that has either onboard Ethernet or wifi, so I can utilize this library: https://github.com/ChuckBell/MySQL_Connector_Arduino

Then I'll be able to populate the database with live temperature data!

Docker containers to be included:

- Sensor processing

- Redis

- Node.js web server

- Optional application to write values to external MySQL database

## Hardware

### Board

- [Arduino MKR1000](https://store-usa.arduino.cc/collections/boards/products/arduino-mkr1000-wifi-with-headers-mounted)

OR

- Orange Pi (Zero)


### Sensor

- [DHT11 sensor](https://www.amazon.com/Temperature-Humidity-Digital-3-3V-5V-Raspberry/dp/B07WT2HJ4F/ref=sr_1_1?keywords=dht11+sensor&qid=1638560461&sr=8-1)

OR

- [DHT22 sensor](https://www.adafruit.com/product/385)

### Miscellaneous

- Breadboard

- Jumper wires

- 10k ohm resistor (pull-up)

## TODO:

- Clean up and add Arduino code

- deploy Arduino code from setup script? Board setup via wifi?

- finish setup script

- finish .env and docker-compose

- write new Orange Pi Python library for DHT11 and DHT22 support

- Dockerize Redis
