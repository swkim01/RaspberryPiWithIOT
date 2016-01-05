TCPClient client;
// IP 주소를 문자열로 변환하는 함수
void ipArrayFromString(byte ipArray[], String ipString) {
    int dot1 = ipString.indexOf('.');
    ipArray[0] = ipString.substring(0, dot1).toInt();
    int dot2 = ipString.indexOf('.', dot1 + 1);
    ipArray[1] = ipString.substring(dot1 + 1, dot2).toInt();
    dot1 = ipString.indexOf('.', dot2 + 1);
    ipArray[2] = ipString.substring(dot2 + 1, dot1).toInt();
    ipArray[3] = ipString.substring(dot1 + 1).toInt();
}

// TCP 서버에 접속하는 함수
int connectToMyServer(String ip) {
    byte serverAddress[4];
    ipArrayFromString(serverAddress, ip);
    if (client.connect(serverAddress, 9000)) {
        return 1; // successfully connected
    } else {
        return -1; // failed to connect
    }
}

// connect라는 Spark 함수 등록 및 디지털 출력 핀 설정
void setup() {
    Spark.function("connect", connectToMyServer);
    for (int pin = D0; pin <= D7; ++pin) {
        pinMode(pin, OUTPUT);
    }
}

// 서버로부터 디지털 포트 출력 요청 시 값을 출력
void loop() {
    if (client.connected()) {
        if (client.available()) {
            char pin = client.read() - '0' + D0;
            char level = client.read();
            if ('h' == level) {
                digitalWrite(pin, HIGH);
            } else {
                digitalWrite(pin, LOW);
            }
        }
    }
}
