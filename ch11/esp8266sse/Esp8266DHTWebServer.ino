
#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>
#include <DHT.h>

#define DHTTYPE DHT22
#define DHTPIN 4

const char* ssid = "<SSID>";
const char* password = "<PASSWORD>";

ESP8266WebServer server(80);

DHT dht(DHTPIN, DHTTYPE); // 12 works fine for esp8266

float temp, humi;
String webString = "";
unsigned long previousMillis = 0;
const long interval = 2000;
const int led = 2;
int ledstate = 0;

void handleled() {
  ledstate = !ledstate;
  digitalWrite(led, ledstate);
  Serial.print("led"); Serial.println(ledstate);
  server.send(200, "text/plain", "OK from esp8266!");
}

void handleNotFound() {
  digitalWrite(led, 1);
  String message = "File Not Found\n\n";
  message += "URI: ";
  message += server.uri();
  message += "\nMethod: ";
  message += (server.method() == HTTP_GET) ? "GET" : "POST";
  message += "\nArguments: ";
  message += server.args();
  message += "\n";
  for (uint8_t i = 0; i < server.args(); i++) {
    message += " " + server.argName(i) + ": " + server.arg(i) + "\n";
  }
  server.send(404, "text/plain", message);
  digitalWrite(led, 0);
}

void setup(void) {
  pinMode(led, OUTPUT);
  digitalWrite(led, 0);
  Serial.begin(115200);
  delay(10);
  dht.begin();

  Serial.print("Connecting to ");
  Serial.println(ssid);
  
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  // Wait for connection
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.print("WiFi Connected");
  Serial.println(WiFi.localIP());

  // Start the server
  server.on("/led", handleled);
  server.on("/events", handleevents);
  server.onNotFound(handleNotFound);
  server.begin();
  Serial.println("HTTP server started");
}

void loop(void) {
  server.handleClient();
}

void handleevents() {
  gettemphumi();
  webString="{\"temperature\": \"" + String(temp) + "\", \"humidity\": \"" + String(humi) + "\" }";
  Serial.println(webString);
  server.send(200, "text/plain", webString);
  yield();
}

void gettemphumi() {
  unsigned long currentMillis = millis();
  if (currentMillis - previousMillis >= interval) {
    previousMillis = currentMillis;
    humi = dht.readHumidity();
    temp = dht.readTemperature(false);
    if (isnan(humi) || isnan(temp)) {
      Serial.println("Failed to read dht sensor.");
      return;
    }
  }
}
