int led = D0;

void setup() {
    pinMode(led, OUTPUT);		// LED 핀을 출력 모드로 설정한다
}

void loop() {
    digitalWrite(led, HIGH);		// LED를 켠다
    delay(500);				// 500mS, 즉 0.5초를 기다린다
    digitalWrite(led, LOW);		// LED를 끈다
    delay(500);
}
