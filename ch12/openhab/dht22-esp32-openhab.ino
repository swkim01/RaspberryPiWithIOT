#include <WiFi.h>
#include <string.h>
#include <DHT.h>

#define DHT_SENSOR 4
#define DHT_TYPE DHT22
DHT dht(DHT_SENSOR, DHT_TYPE);

const char* ssid = "<SSID>";
const char* password = "<PASSWORD>";

const char* host = "<HOST IP>";
const int port = 80;
WiFiClient client;

float temp, humi;
String packetString="";
unsigned long requestID = 1;
unsigned long next_heartbeat = 0;
unsigned long sample_time = 10000;

void setup()
{
  Serial.begin(115200);
  Serial.println("\nStarting...");
  while(!Serial) { }

  Serial.println("Initializing DHT sensor.");
  dht.begin();

  // Connect to WiFi network
  Serial.print("Connecting to ");
  Serial.println(ssid);

  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("WiFi connected");

  // Print the IP address
  Serial.println(WiFi.localIP());

  delay(1);
  Serial.print("connecting to ");
  Serial.println(host);

  // Use WiFiClient class to create TCP connections
  if (!client.connect(host, port)) {
    Serial.println("connection failed");
    return;
  }
}

void loop() {
  unsigned long now;

  now = millis();
  if (now < next_heartbeat) return;
  next_heartbeat = millis() + sample_time;
  Serial.println("New packet");
  packetString = "";
  humi = dht.readHumidity();
  temp = dht.readTemperature(false);
  if (isnan(humi) || isnan(temp)) {
    Serial.println("Failed to read dht sensor.");
    return;
  }
  packetString="temperature:" + String(temp) + "C;humidity:" + String(humi) + "P;";
  client.print(packetString);
  Serial.println(packetString);
  requestID = requestID + 1;
}
