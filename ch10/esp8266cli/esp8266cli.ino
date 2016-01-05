#include <ESP8266WiFi.h>
#include <WiFiClient.h>

const char* ssid     = "<SSID>";
const char* password = "<PASSWORD>";

WiFiClient client;
const char* host = "192.168.0.30";		// 서버 IP
unsigned int port = 9999;			// 포트 번호
char wbuf[20];

void setup() {
  Serial.begin(115200);
  delay(10);

  // WiFi 네트워크 연결 시작
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);
  
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected");  
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());

  if (!client.connect(host, port)) {
    Serial.println("connection failed");
    return;
  }
}

void loop() {
  if (Serial.available() > 0) {
    Serial.readBytes(wbuf, 20);
    Serial.print(wbuf);
    client.print(wbuf);
    Serial.println("send ok");
  }
  delay(1000);
}
