
int led=13;
int index=0;
boolean ack = true;

void setup()
{
  Serial.begin(9600);
  pinMode(led, OUTPUT);
  digitalWrite(led, LOW);
}

void loop()
{
  char sb, data[16];
  if (ack == true) {
    digitalWrite(led, HIGH);
    delay(1000);
    Serial.println("REQ");
    ack = false;
  }
  while(Serial.available()) {
    sb = Serial.read();
    data[index++] = sb;
  }
  if (index > 4) {
    if (strncmp(data, "ACK", 3) == 0) {
      digitalWrite(led, LOW);
      ack = true;
      delay(1000);
    }
    index = 0;
  }
}
