#include "TimeAlarms/TimeAlarms.h"

int greenLED = D0;
int yellowLED = D1;
int redLED = D2;


void myHandler(const char *event, const char *data)
{
    Serial.print(event);
    Serial.print(", data: ");
    if (data)
        Serial.println(data);
    else
        Serial.println("NULL");
    turnOnLED(data);
    Alarm.timerOnce(3600, turnOffLED);             // 1시간 후에 한 번 호출
}

void setup() {
    Spark.subscribe("TodaysWeather", myHandler);
    Serial.begin(9600);
    
    pinMode(greenLED, OUTPUT);
    pinMode(yellowLED, OUTPUT);
    pinMode(redLED, OUTPUT);
}

void loop() {
  Alarm.delay(1000); // 알람 처리를 위해 1초 대기
}

void turnOnLED(const char *data)
{
    String str = String(data);
    
    if (str.indexOf("Sunny") >= 0 || str.indexOf("Clear") >= 0) {
        digitalWrite(greenLED, HIGH);      // 녹색 LED를 켬
    }
    else if (str.indexOf("Cloud") >= 0) {
        digitalWrite(yellowLED, HIGH);     // 노란색 LED를 켬

    }
    else if (str.indexOf("Rain") >= 0 || str.indexOf("Shower") >= 0 || str.indexOf("Snow") >= 0) {
        digitalWrite(redLED, HIGH);        // 빨간색 LED를 켬
    }
    
}

void turnOffLED()
{
    digitalWrite(greenLED, LOW);           // 녹색 LED를 끔
    digitalWrite(yellowLED, LOW);          // 노란색 LED를 끔
    digitalWrite(redLED, LOW);             // 빨간색 LED를 끔
}
