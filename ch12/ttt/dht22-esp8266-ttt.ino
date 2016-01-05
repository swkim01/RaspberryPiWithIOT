#include <SoftwareSerial.h>
#include <ESP8266.h>
#include <DHT.h>

unsigned long requestID = 1;
unsigned long next_heartbeat = 0;
unsigned long sample_time = 30000;

#define DHT_SENSOR   A2
#define DHT_TYPE     DHT22
DHT dht(DHT_SENSOR, DHT_TYPE);

prog_char * const loopPacket1 PROGMEM = "{\"path\":\"/api/v1/thing/reporting\",\"requestID\":\"";
prog_char * const loopPacket2 PROGMEM = "\",\"things\":{\"/device/climate/arduino/meteo\":{\"prototype\":{\"device\":{\"name\":\"Arduino Dht11 Sensor\",\"maker\":\"Arduino\"},\"name\":\"true\",\"status\":[\"present\",\"absent\",\"recent\"],\"properties\":{\"temperature\":\"celcius\",\"humidity\":\"percent\"}},\"instances\":[{\"name\":\"Arduino Dht11 Sensor\",\"status\":\"present\",\"unit\":{\"serial\":\"";
prog_char * const loopPacket3 PROGMEM = "\",\"udn\":\"195a42b0-ef6b-11e2-99d0-";
prog_char * const loopPacket4 PROGMEM = "-dht11\"},\"info\":{\"temperature\":";
prog_char * const loopPacket5 PROGMEM = ",\"humidity\":";
prog_char * const loopPacket6 PROGMEM = "},\"uptime\":";
prog_char * const loopPacket7 PROGMEM = "}]}}}";

IPAddress host(224,0,9,1);
unsigned int port = 22601;
#define WLAN_SSID       "<SSID>"           // cannot be longer than 32 characters!
#define WLAN_PASS       "<PASSWORD>"
#define WLAN_SECURITY   WLAN_SEC_WPA2

SoftwareSerial esp8266Serial = SoftwareSerial(2, 3);
ESP8266 wifi = ESP8266(esp8266Serial);
char packetBuffer[512];

void setup(void)
{
  Serial.begin(9600);
  Serial.println("Initializing DHT sensor.");
  dht.begin();

  /* Initialise the module */
  Serial.println(F("\nInitializing..."));
  esp8266Serial.begin(9600);
  wifi.begin();
  wifi.setTimeout(1000);
  // setWifiMode
  Serial.print("setWifiMode: ");
  Serial.println(getStatus(wifi.setMode(ESP8266_WIFI_STATION)));
  // joinAP
  Serial.print(F("\nAttempting to connect to ")); Serial.println(WLAN_SSID);
  Serial.println(getStatus(wifi.joinAP(WLAN_SSID, WLAN_PASS)));
  Serial.println(F("Connected!"));
  // connect
  Serial.print("connect: ");
  Serial.println(getStatus(wifi.connect(ESP8266_PROTOCOL_UDP, host, port)));
  
  next_heartbeat = millis() + sample_time;
}

void loop(void)
{
  float humidity=20, temperature=25;
  char  buffer[24];
  unsigned long now;

  now = millis();
  if (now < next_heartbeat) return;
  next_heartbeat = millis() + sample_time;

  humidity = dht.readHumidity();
  temperature = dht.readTemperature();

  strcpy(packetBuffer,(char*)pgm_read_word(&loopPacket1) );
  strcat(packetBuffer, ultoa( requestID, buffer, 10) );
  strcat(packetBuffer,(char*)pgm_read_word(&loopPacket2) );
  for (byte thisByte = 0; thisByte < 6; thisByte++) {
    sprintf(buffer, "%02x", mac[thisByte] );
    strcat(packetBuffer, buffer);
  }
  strcat(packetBuffer,(char*)pgm_read_word(&loopPacket3) );
  for (byte thisByte = 0; thisByte < 6; thisByte++) {
    sprintf(buffer, "%02x", mac[thisByte] );
    strcat(packetBuffer, buffer);
  }
  if (!isnan(temperature)) {
    strcat(packetBuffer,(char*)pgm_read_word(&loopPacket4) );
    strcat(packetBuffer, dtostrf((double) temperature, 4, 2, buffer));
  }
  if (!isnan(humidity)) {
    strcat(packetBuffer,(char*)pgm_read_word(&loopPacket5) );
    strcat(packetBuffer, dtostrf((double) humidity, 4, 2, buffer));
  }
  strcat(packetBuffer,(char*)pgm_read_word(&loopPacket6) );
  strcat(packetBuffer, ultoa( now, buffer, 10) );
  strcat(packetBuffer,(char*)pgm_read_word(&loopPacket7) );

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

