int ledPin = D7;
int dhtPin = D0;
int ledStatus = 0;
double humidity = 0;
double temperature = 0;
int ms = 0;
void setup()
{
    Spark.function("led", ledControl);
    pinMode(ledPin, OUTPUT);
    // LED OFF로 초기화
    digitalWrite(ledPin, LOW);

    Spark.variable("humidity", &humidity, DOUBLE);
    Spark.variable("temperature", &temperature, DOUBLE);
    pinMode(dhtPin, INPUT_PULLUP);
    
    Serial.begin(9600);
}
void loop()
{
    char temp[10], humi[10];
    
    if (millis() - ms > 10000) {
        read_dht(dhtPin, &humidity, &temperature);
        Serial.print("LED: ");
        Serial.print(ledStatus);
        Serial.print(" - Humidity: ");
        Serial.print(humidity);
        Serial.print("% - Temperature: "); 
        Serial.print(temperature);
        Serial.print("*C ");
        Serial.println(Time.timeStr());
        //sprintf(temp, "%.2f", temperature);
        //sprintf(humi, "%.2f", humidity);
        //Spark.publish("temperature", temp);
        //Spark.publish("humidity", humi);
        ms = millis();
    }
}

// The parameter must be HIGH or LOW
int ledControl(String parameter)
{
   if(parameter.substring(0,4) == "HIGH") {
       digitalWrite(ledPin, HIGH);
       ledStatus = 1;
   } else if(parameter.substring(0,3) == "LOW") {
       digitalWrite(ledPin, LOW);
       ledStatus = 0;
   } else
       return -1;
   return 1;
}

int read_dht(int pin, double *humidity, double *temperature)
{
    uint8_t data[5] = {0, 0, 0, 0, 0};
    noInterrupts();
    pinMode(pin, OUTPUT);
    digitalWrite(pin, LOW);
    delay(20);
    pinMode(pin, INPUT_PULLUP);
    if (detect_edge(pin, HIGH, 10, 200) == -1) {
        return -1;
    }
    if (detect_edge(pin, LOW, 10, 200) == -1) {
        return -1;
    }
    if (detect_edge(pin, HIGH, 10, 200) == -1) {
        return -1;
    }
    for (uint8_t i = 0; i < 40; i++) {
        if (detect_edge(pin, LOW, 10, 200) == -1) {
            return -1;
        }
        int counter = detect_edge(pin, HIGH, 10, 200);
        if (counter == -1) {
            return -1;
        }
        data[i/8] <<= 1;
        if (counter > 4) {
            data[i/8] |= 1;
        }
    }
    interrupts();
    if (data[4] != ((data[0] + data[1] + data[2] + data[3]) & 0xFF)) {
        return -1;
    }
    *humidity = (double)data[0];
    *temperature = (double)data[2];
    return 0;
}

int detect_edge(int pin, int val, int interval, int timeout)
{
    int counter = 0;
    while (digitalRead(pin) == val && counter < timeout) {
        delayMicroseconds(interval);
        ++counter;
    }
    if (counter > timeout) {
        return -1;
    }
    return counter;
}
