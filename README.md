# temperature-data-collector
An open-source DIY weather station, consisting of lightweight collectors and a Dockerized sensor Hub (MQTT + web dashboard). Currently collects temperature and humidity data, while barometric pressure and air quality are on the roadmap.

This is an all-in-one project which includes: collectors for various hardware platforms, an MQTT system (server, subscribers, publishers), Redis server, the ability to write to MySQL, and a web server to monitor live data.

There are two components: Collector, and Server.

### Collector

- Arduino sensor collector

OR

- Orange Pi sensor collector (deprecated)

### Server ("Hub")

- MQTT server

- MQTT subscriber

- Redis server

- Node.js web server

- (Optional, not included) MySQL server

![Container diagram](temperature-data-collector-1.jpg)


## Hardware

### Board

- [Arduino MKR1000](https://store-usa.arduino.cc/collections/boards/products/arduino-mkr1000-wifi-with-headers-mounted)

OR

- [Orange Pi (Zero)](https://a.co/d/6ztEWGC)


### Sensor

- [DHT22 sensor](https://www.adafruit.com/product/385)

	- DHT11s were supported in the Orange Pi version, but will not be supported going forward.

- [BME280 sensor](https://www.adafruit.com/product/2652)

	- For barometric pressure. Not supported yet, but will be shortly! Probably will replace the DHT22.


### Miscellaneous

- Breadboard

- Jumper wires

- 10k ohm resistor (pull-up)

- Optional: Status LED and 220 ohm resistor


### Enclosures

Coming soon


### DHT circuit diagram

![DHT circuit](dht-circuit.jpg)

[Image source](https://osoyoo.com/2017/07/19/arduino-lesson-dht11-sensor/)


## How it runs

Collector code is in the `collector` or `collector-esp32` directory.

Server is everything else (web, redis, etc) and can be run via docker-compose (or each component standalone).

Collectors send data via MQTT to the server. The MQTT subscriber then adds to redis and exports to MySQL (optional). The web server will read from redis.


## Getting started

The server must be running first, or the collector won't be able to make a connection to the MQTT server.

Server:

1. Clone and enter this repository on your server

2. If you have a firewall, two TCP ports need to be opened: 1883 for receiving collector messages, and 8080 for the web server.

3. Run `docker-compose up --build`

4. Server is ready to accept new connections from collectors, and the web server should be visible at `http://server_ip:8080`


Collector (ESP32 / Arduino):
1. Install any prerequisite libraries (list coming soon)

2. Fill in your MQTT and Wifi credentials

3. Flash the code in `collector-esp32/collector.ino` to your board.

NOTE: The device goes into low power mode to save battery, so if you need to flash again, double-tap the button on the board to go into bootloader mode to ensure continuous connection to your PC.


Collector (Orange Pi):

1. Build the circuit in the "Circuit diagram" section above, with a 10k ohm resistor, DHT sensor, and Orange Pi. Have the data pin going to the proper GPIO port (the collector defaults to PA6)

2. Connect the Orange Pi to a network. WiFi makes the device more useful, you can use a wifi config tool such as nmtui. For first-time setup, or if your device doesn't have nmtui installed yet, connect via Ethernet first.

3. On the Orange Pi, clone this repository and run collector/collector.py. Edit the script if you would like to change the sensor model, GPIO port, sample rate, etc.

4. You should get temperature and humidity values as output, and the data will be published via MQTT for the listening server.


## Development notes

For V1:

- Server: finish credential management (.env files, and their usage in docker-compose)

- Server: finish setup script

- Server: MySQL export functionality in MQTT subscriber

- Collector: Model files for casing / outdoor placement

- Collector: Credential management

- Collector: Barometric pressure sensor

- Collector: Batteries

- Collector: Phase out / fully deprecate Orange Pi version

- Branding


For V2:

- Collector: Solar

- Collector: AQI sensors

- Server: Modular "hub" to make platform more accessible