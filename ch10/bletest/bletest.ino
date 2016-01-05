#include <SoftwareSerial.h>
#define rxPin 2
#define txPin 3
SoftwareSerial bleSerial(rxPin, txPin); // RX, TX 레오나르도 보드는 rxPin으로 8, 9, 10, 11, 14, 15, 16 핀을 사용할 수 있다.

void setup()
{
  Serial.begin(9600);
  pinMode (rxPin, INPUT);
  pinMode (txPin, OUTPUT);

  bleSerial.begin(9600);
  // 슬레이브 설정
  bleserial.print("AT+ROLE0");
  // 또는 마스터 설정
  // bleserial.print("AT+ROLE1");
  delay(10000);
}

void loop()
{
  if (bleSerial.available())
    Serial.write(bleSerial.read());
  if (Serial.available())
    bleSerial.write(Serial.read());
}
