# DHT-display-server
A Node.js server to display humidity and temperature data from a digital temperature and humidity sensor (DHT)

Currently pulling pre-inserted test data from a MySQL database, until I get the Arduino component working. Need to acquire a new Arduino that has either onboard Ethernet or wifi, so I can utilize this library: https://github.com/ChuckBell/MySQL_Connector_Arduino

Then I'll be able to populate the database with live temperature data!

## Hardware
-[Arduino MKR1000](https://store-usa.arduino.cc/collections/boards/products/arduino-mkr1000-wifi-with-headers-mounted)

OR

-Orange Pi (Zero)

-[DHT11 sensor](https://www.amazon.com/Temperature-Humidity-Digital-3-3V-5V-Raspberry/dp/B07WT2HJ4F/ref=sr_1_1?keywords=dht11+sensor&qid=1638560461&sr=8-1)

-Breadboard

-Jumper wires

-10k ohm resistor (pull-up)

-Ubuntu server to run the web server and database on

## TODO:

-Add Arduino code here

-deploy Arduino code from setup script? Board setup via wifi?

-finish setup script

-Orange Pi (use python script which will be included, using the DHT11-Python-library-Orange-PI library)
