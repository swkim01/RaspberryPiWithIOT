#include <WiFi.h>
#include <WiFiClient.h>
#include <DHT.h>
#define DHTTYPE DHT22
#define DHTPIN 4

#define EVENT_NAME "alarm"
#define KEY "<KEY>"

const char* ssid = "<SSID>";
const char* password = "<PASSWORD>";

WiFiClient client;
// 온도 센서 객체 생성
DHT dht(DHTPIN, DHTTYPE);

float temp, humi;
unsigned long previousMillis = 0;
const long interval = 2000;

void setup() {
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
  // IP 주소 출력
  Serial.println(WiFi.localIP());
}

void loop() {
  gettemphumi();
  if (temp > 32) {
    Serial.println("Very Hot");
    if (client.connect("maker.ifttt.com",80)) {
      Serial.println("Connected to Maker");
      sendTrigger();
    } else {
      Serial.println("Failed to connect to Maker.");
    }
  }
  Serial.println("temperature:"+String(temp)+", humidity:"+String(humi));
  delay(10000);
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

void sendTrigger()
{
  // 패킷은 다음과 비슷한 형태로 구성:
  //
  // POST /trigger/ESP/with/key/(myKey) HTTP/1.1
  // Host: maker.ifttt.com
  // User-Agent: ESP32_Thing
  // Connection: close
  // Conent-Type: application/json
  // Conent-Length: (postData length)
  //
  // {"value1":temperature, "value2":humidity )"}
  String postData = "{\"value1\":";
  postData.concat(String(temp));
  postData.concat(",\"value2\":");
  postData.concat(String(humi));
  postData.concat("}");

  client.print("POST /trigger/");
  client.print(EVENT_NAME);
  client.print("/with/key/");
  client.print(KEY);
  client.println(" HTTP/1.1");
  client.println("Host: maker.ifttt.com");
  client.println("User-Agent: ESP32_Thing");
  client.println("Connection: close");
  client.println("Content-Type: application/json");
  client.print("Content-Length: ");
  client.println(postData.length());
  client.println();
  client.println(postData);
}
