#include <ESP8266.h>
#include <SoftwareSerial.h>

IPAddress host(192,168,0,30);			// 서버 IP
unsigned int port = 9999;			// 서버 포트 번호
#define WLAN_SSID       "<공유기 SSID>"
#define WLAN_PASS      "<패스워드>"
#define WLAN_SECURITY   WLAN_SEC_WPA2
SoftwareSerial esp8266Serial = SoftwareSerial(2, 3);
ESP8266 wifi = ESP8266(esp8266Serial);
byte mac[6];
char wbuf[20];

void setup(void)
{
  Serial.begin(9600);
  
  /* Initialise the module */
  Serial.println(F("\nInitializing..."));
  esp8266Serial.begin(9600);
  wifi.begin();
  wifi.setTimeout(1000);
  
  // setWifiMode
  Serial.print("setWifiMode: ");
  Serial.println(getStatus(wifi.setMode(ESP8266_WIFI_STATION)));
  
  wifi.getMAC(ESP8266_WIFI_STATION, mac);
  Serial.print("MAC address      : ");
  for (byte thisByte = 0; thisByte < 6; thisByte++) {
    if (thisByte != 0) Serial.print(":");
    if (mac[thisByte] < 0x0a) Serial.print("0");
    Serial.print(mac[thisByte], HEX);
  }
  Serial.println();
  
  // joinAP
  Serial.print(F("\nAttempting to connect to ")); Serial.println(WLAN_SSID);
  Serial.println(getStatus(wifi.joinAP(WLAN_SSID, WLAN_PASS)));
  Serial.println(F("Connected!"));
  
  // connect
  Serial.print("connect: ");
  Serial.println(getStatus(wifi.connect(ESP8266_PROTOCOL_TCP, host, port)));
  
  delay(2000);
}

void loop(void)
{
  if (Serial.available() > 0) {
    Serial.readBytes(wbuf, 20);
    Serial.print(wbuf);
    wifi.send(wbuf);
    Serial.flush();
  }
  delay(1000);
}

String getStatus(ESP8266CommandStatus status)
{
  switch (status) {
  case ESP8266_COMMAND_INVALID:   return "INVALID";		   break;
  case ESP8266_COMMAND_TIMEOUT:   return "TIMEOUT";		   break;
  case ESP8266_COMMAND_OK: 	  return "OK";			   break;
  case ESP8266_COMMAND_NO_CHANGE: return "NO CHANGE";		   break;
  case ESP8266_COMMAND_ERROR: 	  return "ERROR";		   break;
  case ESP8266_COMMAND_NO_LINK:   return "NO LINK";		   break;
  case ESP8266_COMMAND_TOO_LONG:  return "TOO LONG";		   break;
  case ESP8266_COMMAND_FAIL: 	  return "FAIL";		   break;
  default: 			  return "UNKNOWN COMMAND STATUS"; break;
  }
}
