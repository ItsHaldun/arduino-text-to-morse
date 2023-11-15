#define OUTPUT_PIN 2

void setup() {
  pinMode(OUTPUT_PIN, OUTPUT);
  digitalWrite(OUTPUT_PIN, LOW);

  Serial.begin(9600);
}

void loop() {
}

void serialEvent() {
  while (Serial.available()) {
    // get the new byte:
    char state = (char)Serial.read();
    if (state == 'g') {
      if (digitalRead(OUTPUT_PIN) == HIGH) {
        digitalWrite(OUTPUT_PIN, LOW);
      } 
      else {
        digitalWrite(OUTPUT_PIN, HIGH);
      }
    }
  }
}
