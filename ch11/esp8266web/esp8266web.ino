#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>
#include <DHT.h>

#define DHTTYPE DHT22
#define DHTPIN 2

const char* ssid = "<SSID>";
const char* password = "<PASSWORD>";

// 서버 객체 생성, 인자로 포트 지정
ESP8266WebServer server(80);

// DHT 객체 생성
DHT dht(DHTPIN, DHTTYPE, 12); // esp8266을 위해 12 지정

float temp, humi;
String webString="";
unsigned long previousMillis = 0;
const long interval = 2000;
const int led = 13;
int ledstate = 0;

void setup() {
  pinMode(led, OUTPUT);
  digitalWrite(led, 0);
  Serial.begin(115200);
  delay(10);
  dht.begin();
  
  // WiFi 네트워크 연결
  Serial.print("Connecting to ");
  Serial.println(ssid);
  
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected");
  
  // 서버 시작
  server.on("/led", handleled);
  server.on("/events", handleevents);
  server.begin();

  // IP 주소 출력
  Serial.println(WiFi.localIP());
}

void loop() {
  server.handleClient();
}

void handleled() {
  ledstate = !ledstate;
  digitalWrite(led, ledstate);
  Serial.println("led" + ledstate);
  server.send(200, "text/plain", "OK");
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
