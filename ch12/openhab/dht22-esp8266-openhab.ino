#include <SoftwareSerial.h>
#include <ESP8266.h>
#include <string.h>
#include <DHT.h>

unsigned long requestID = 1;
unsigned long next_heartbeat = 0;
unsigned long sample_time = 30000;

#define DHT_SENSOR   A2
#define DHT_TYPE     DHT22
DHT dht(DHT_SENSOR, DHT_TYPE);

SoftwareSerial esp8266Serial = SoftwareSerial(2, 3);
ESP8266 wifi = ESP8266(esp8266Serial);

PROGMEM prog_char *loopPacket1 = "temperature:";
PROGMEM prog_char *loopPacket2 = "C;humidity:";
PROGMEM prog_char *loopPacket3 = "P;";

IPAddress host(192,168,0,30);
unsigned int port = 3000;
#define WLAN_SSID       "<SSID>"          // cannot be longer than 32 characters!
#define WLAN_PASS       "<패스워드>"
#define WLAN_SECURITY   WLAN_SEC_WPA2

IPAddress ip;
char packetBuffer[30];

void setup()
{
  Serial.begin(9600);
  Serial.println("\nStarting...");
  while(!Serial) { }

  Serial.println("Initializing DHT sensor.");
  dht.begin();

  // ESP8266
  Serial.println(F("\nInitializing..."));
  esp8266Serial.begin(9600);
  wifi.begin();

  // setWifiMode
  Serial.print("setWifiMode: ");
  Serial.println(getStatus(wifi.setMode(ESP8266_WIFI_STATION)));
  
  // joinAP
  Serial.print(F("\nAttempting to connect to ")); Serial.println(WLAN_SSID);
  Serial.println(getStatus(wifi.joinAP(WLAN_SSID, WLAN_PASS)));
   
  Serial.println(F("Connected!"));
  wifi.getIP(ESP8266_WIFI_STATION, ip);
  Serial.println(ip);
  // connect
  Serial.print("connect: ");
  Serial.println(getStatus(wifi.connect(ESP8266_PROTOCOL_TCP, host, port)));
  
  next_heartbeat = millis() + sample_time;
}

void loop() {
  float humidity, temperature;
  char  buffer[24];
  unsigned long now;

  now = millis();
  if (now < next_heartbeat) return;
  next_heartbeat = millis() + sample_time;

  humidity = dht.readHumidity();
  temperature = dht.readTemperature();

  strcpy(packetBuffer,(char*)pgm_read_word(&loopPacket1) );
  if (!isnan(temperature)) {
     strcat(packetBuffer, dtostrf((double) temperature, 4, 2, buffer));
  }
  strcat(packetBuffer,(char*)pgm_read_word(&loopPacket2) );
  if (!isnan(humidity)) {
    strcat(packetBuffer, dtostrf((double) humidity, 4, 2, buffer));
  }
  strcat(packetBuffer,(char*)pgm_read_word(&loopPacket3) );

  int n = strlen(packetBuffer);
  Serial.print("writing ");Serial.print(n);Serial.println(" octets");
  Serial.println(packetBuffer);
  Serial.println(getStatus(wifi.send(packetBuffer)));
  requestID = requestID + 1;
}

String getStatus(bool status)
{
  if (status)
    return "OK";
  return "KO";
}

String getStatus(ESP8266CommandStatus status)
{
  switch (status) {
  case ESP8266_COMMAND_INVALID: return "INVALID"; break;
  case ESP8266_COMMAND_TIMEOUT: return "TIMEOUT"; break;
  case ESP8266_COMMAND_OK: return "OK"; break;
  case ESP8266_COMMAND_NO_CHANGE: return "NO CHANGE"; break;
  case ESP8266_COMMAND_ERROR: return "ERROR"; break;
  case ESP8266_COMMAND_NO_LINK: return "NO LINK"; break;
  case ESP8266_COMMAND_TOO_LONG: return "TOO LONG"; break;
  case ESP8266_COMMAND_FAIL: return "FAIL"; break;
  default: return "UNKNOWN COMMAND STATUS"; break;
  }
}
