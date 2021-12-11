# temperature-data-collector
An application intended for a custom-built IoT device, to collect, process, and display temperature and humidity data from a digital temperature and humidity sensor (DHT)

This is an all-in-one project including collectors for various hardware platforms, a Redis server, a MySQL exporter, and a web server to monitor live data.

Docker containers to be included:

- Pi sensor collector

- Arduino sensor collector

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

	- Recommended. DHT22s are much more accurate, for only a tiny bit more.

### Miscellaneous

- Breadboard

- Jumper wires

- 10k ohm resistor (pull-up)

## TODO:

- Clean up and add Arduino code

- deploy Arduino code from setup script? Board setup via wifi?

- finish setup script

- finish .env and docker-compose

- Python collector - store in Redis

- finish new Orange Pi Python library for DHT11 and DHT22 support

- Dockerize Redis

Note: For Arduino+MySQL, utilize this library: https://github.com/ChuckBell/MySQL_Connector_Arduino
