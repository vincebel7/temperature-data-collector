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
const unsigned long publishInterval = 10;

char macStr[18];
byte mac[6];

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

  WiFi.macAddress(mac);
  sprintf(macStr, "%02X:%02X:%02X:%02X:%02X:%02X", mac[0], mac[1], mac[2], mac[3], mac[4], mac[5]);
}

void loop() {
  // --- Ensure WiFi connection ---
  if (WiFi.status() != WL_CONNECTED) {
    Serial.println("Connecting to WiFi...");
    WiFi.disconnect();
    WiFi.begin(ssid, pass);

    unsigned long startAttempt = millis();
    while (WiFi.status() != WL_CONNECTED && millis() - startAttempt < 10000) { // 10s timeout
      delay(500);
      Serial.print(".");
    }
    if (WiFi.status() == WL_CONNECTED) {
      Serial.println(" WiFi connected!");
      Serial.print("IP: ");
      Serial.println(WiFi.localIP());
    } else {
      Serial.println(" WiFi failed, going to sleep...");
      WiFi.disconnect();
      LowPower.sleep(publishInterval * 1000);
      return;
    }
  }

  // --- Ensure MQTT connection ---
  if (!mqttClient.connected()) {
    mqttClient.setUsernamePassword(mqttUser, mqttPass);
    Serial.println("Connecting to MQTT...");
    if (!mqttClient.connect(broker, port)) {
      Serial.print("MQTT failed, code = ");
      Serial.println(mqttClient.connectError());
      WiFi.disconnect();
      LowPower.sleep(publishInterval * 1000);
      return;
    }
    Serial.println("MQTT connected");
  }

  // --- Read DHT22 safely ---
  float h = dht.getHumidity();
  float t = dht.getTemperature();

  if (isnan(h) || isnan(t)) {
    Serial.println("Sensor read error, skipping publish");
    WiFi.disconnect();
    LowPower.sleep(publishInterval * 1000);
    return;
  }

  // --- Build JSON message ---
  String msg = "{";
  msg += "\"id\": " + String(macStr) + ",";
  msg += "\"temperature\": " + String(t, 1) + ",";
  msg += "\"humidity\": " + String(h, 1) + ",";
  msg += "\"pressure\": " + String(0); // placeholder
  msg += "}";

  // --- Publish ---
  mqttClient.beginMessage(topic);
  mqttClient.print(msg);
  mqttClient.endMessage();

  Serial.print("Published: ");
  Serial.println(msg);

  // --- Blink LED once ---
  digitalWrite(LEDPIN, HIGH);
  delay(200);
  digitalWrite(LEDPIN, LOW);

  // --- Disconnect to save power ---
  mqttClient.stop();
  WiFi.disconnect();
  WiFi.end();

  Serial.println("Sleeping...");
  //LowPower.idle(publishInterval * 1000); // Doesn't work reliably on MKR1000, maybe for ESP32
  delay(publishInterval * 1000);
}