#include <WiFi101.h>
#include <ArduinoMqttClient.h>
#include <DHT22.h>
#include <RTCZero.h>
#include <ArduinoLowPower.h>

#define LEDPIN A5
#define DHTPIN A6
DHT22 dht(DHTPIN);

char ssid[] = "";
char pass[] = "";

const char broker[] = "";
const char mqttUser[] = "";
const char mqttPass[] = "";
int port = 1883;
const char topic[] = "General";

WiFiClient wifiClient;
MqttClient mqttClient(wifiClient);

// Publish interval (seconds)
const unsigned long publishInterval = 30;

void setup() {
  pinMode(LEDPIN, OUTPUT);
  digitalWrite(LEDPIN, LOW);

  Serial.begin(115200);

  // Boot indicator
  for (int i = 0; i < 3; i++) {
    digitalWrite(LEDPIN, HIGH);
    delay(200);
    digitalWrite(LEDPIN, LOW);
    delay(200);
  }
}

void loop() {
  // Connect WiFi
  WiFi.begin(ssid, pass);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("WiFi connected");

  // Connect MQTT
  mqttClient.setUsernamePassword(mqttUser, mqttPass);
  if (!mqttClient.connect(broker, port)) {
    Serial.print("MQTT connection failed, code = ");
    Serial.println(mqttClient.connectError());
    WiFi.disconnect();
    LowPower.sleep(publishInterval * 1000);
    return; // try again on next cycle
  }

  // Read DHT22
  float h = dht.getHumidity();
  float t = dht.getTemperature();

  if (!isnan(h) && !isnan(t)) {
    String msg = "{";
    msg += "\"time\": " + String(millis()) + ",";
    msg += "\"temperature\": " + String(t, 1) + ",";
    //msg += "\"humidity\": " + String(h, 1);
    msg += "\"humidity\": " + String(h, 1) + ",";
    msg += "\"pressure\": " + String(0); // Placeholder for pressure sensor
    msg += "}";

    mqttClient.beginMessage(topic);
    mqttClient.print(msg);
    mqttClient.endMessage();

    Serial.print("Published: ");
    Serial.println(msg);

    // Flash LED once
    digitalWrite(LEDPIN, HIGH);
    delay(200);
    digitalWrite(LEDPIN, LOW);
  }

  mqttClient.stop();
  WiFi.disconnect();

  Serial.println("Sleeping...");
  LowPower.sleep(publishInterval * 1000);
}

