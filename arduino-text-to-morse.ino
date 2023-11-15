#define BUZZER 2
#define BUFFER_SIZE 2048

int buffer[BUFFER_SIZE];
int bufferWriter;
int bufferReader;

void setup() {
  pinMode(BUZZER, OUTPUT);
  noTone(BUZZER);

	int bufferWriter = 0;
	int bufferReader = 0;

  Serial.begin(9600);
}

void loop() {
}

void serialEvent() {
  while (Serial.available()) {
    // get the new byte:
    char state = (char)Serial.read();
    if (state == 'g') {
      if (digitalRead(BUZZER) != LOW) {
        noTone(BUZZER);
      } 
      else {
        tone(BUZZER, 600);
      }
    }
  }
}

// Resets the buffer by copying the contents betweem
// bufferReader and Buffer Writer
void bufferReset() {
}
