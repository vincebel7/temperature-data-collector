# temperature-data-collector
An application enabling a custom-built IoT device to collect, process, and display temperature and humidity data from a digital temperature and humidity sensor (DHT)

This is an all-in-one project which includes: collectors for various hardware platforms, an MQTT system (server, subscribers, publishers), Redis server, the ability to write to MySQL, and a web server to monitor live data.

There are two components: Collector, and Server.

### Collector

- Pi sensor collector

OR

- Arduino sensor collector (not written yet)

### Server

- MQTT server

- MQTT subscriber

- Redis server

- Node.js web server

- (Optional, not included) MySQL server

![Container diagram](temperature-data-collector-1.jpg)


## Hardware

### Board

- [Orange Pi (Zero)](https://a.co/d/6ztEWGC)

OR

- [Arduino MKR1000](https://store-usa.arduino.cc/collections/boards/products/arduino-mkr1000-wifi-with-headers-mounted)


### Sensor

- [DHT11 sensor](https://www.amazon.com/Temperature-Humidity-Digital-3-3V-5V-Raspberry/dp/B07WT2HJ4F/ref=sr_1_1?keywords=dht11+sensor&qid=1638560461&sr=8-1)

OR

- [DHT22 sensor](https://www.adafruit.com/product/385)

	- Recommended. DHT22s are much more accurate, for only a tiny bit more.


### Miscellaneous

- Breadboard

- Jumper wires

- 10k ohm resistor (pull-up)


### DHT circuit diagram

![DHT circuit](dht-circuit.jpg)

[Image source](https://osoyoo.com/2017/07/19/arduino-lesson-dht11-sensor/)


## How it runs

Collector code is in the `collector` directory. This is just a Python script.

Server is everything else (web, redis, etc) and can be run via docker-compose (or each component standalone).

Collectors send data via MQTT to the server. The MQTT subscriber then adds to redis and exports to MySQL (optional). The web server will read from redis.


## Getting started

The server must be running first, or the collector won't be able to make a connection to the MQTT server.

Server:

1. Clone and enter this repository on your server

2. If you have a firewall, two TCP ports need to be opened: 1883 for receiving collector messages, and 8080 for the web server.

3. Run `docker-compose up --build`

4. Server is ready to accept new connections from collectors, and the web server should be visible at `http://server_ip:8080`


Collector:

1. Build the circuit in the "Circuit diagram" section above, with a 10k ohm resistor, DHT sensor, and Orange Pi. Have the data pin going to the proper GPIO port (the collector defaults to PA6)

2. Connect the Orange Pi to a network. WiFi makes the device more useful, you can use a wifi config tool such as nmtui. For first-time setup, or if your device doesn't have nmtui installed yet, connect via Ethernet first.

3. On the Orange Pi, clone this repository and run collector/collector.py. Edit the script if you would like to change the sensor model, GPIO port, sample rate, etc.

4. You should get temperature and humidity values as output, and the data will be published via MQTT for the listening server.


## Development notes

For V1:

- Server: finish credential management (.env files, and their usage in docker-compose)

- Server: finish setup script

- Server: MySQL export functionality in MQTT subscriber

- Model files for casing / outdoor placement


For V2:

- Collector: Finish Arduino platform (or ESP32?)

- Arduino + setup script? Board setup via wifi?
