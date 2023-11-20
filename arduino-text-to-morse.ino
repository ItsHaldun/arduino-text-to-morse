// Pinouts
#define BUZZER 2					// Buzzer output signal pin
#define LED 13
#define SPEED_PIN 0				// Analog Potentiometer input	

// Farnsworth Timings
#define dit 1 		// Units
#define dah 3			// 3 units
#define intra 1		// 1 unit
#define inter 3		// 3 units
#define space 7		// 7 units

// Speed Control (Maybe put on a potentiometer?)
#define WPM 10.0									// Words per minute (PARIS Standard)
#define t_unit 60000.0/(50.0*WPM)	// Miliseconds per unit

#define BUFFER_SIZE 1024
#define FREQUENCY 600

char buffer[BUFFER_SIZE];
int bufferWriter;
int bufferReader;


void setup() {
	// Set up the signal outputs
  pinMode(BUZZER, OUTPUT);
	pinMode(LED, OUTPUT);
	noTone(BUZZER);
	digitalWrite(LED, LOW);

	// Set up buffer R/W
	int bufferWriter = 0;
	int bufferReader = 0;

	// Start serial connection
  Serial.begin(9600);
	
}

void loop() {
	// Read the buffer if there is something to read
	if (bufferReader<bufferWriter) {
		char c = buffer[bufferReader];
		float time = char_to_time(c);
		send_code(time);
		bufferReader++;
	}
}

void serialEvent() {
  while (Serial.available()) {
    // get the new byte:
    char state = (char)Serial.read();

		// Check if valid character
		if (state=='.' || state=='_' || state=='i' || state=='j' || state==' ') {
			if (bufferWriter >= BUFFER_SIZE) {
				bufferReset();
			}
			buffer[bufferWriter] = state;
			bufferWriter++;
		}
  }
}

// Resets the buffer by copying the contents betweem
// bufferReader and Buffer Writer
void bufferReset() {
	int readWriteDiff = bufferWriter - bufferReader;
	for (int i=0; i<readWriteDiff; i++) {
		buffer[i] = buffer[i+bufferReader];
	}
	bufferReader = 0;
	bufferWriter = readWriteDiff;
}

void send_code(float time) {
	if (time>0) {
			tone(BUZZER, FREQUENCY);
			digitalWrite(LED_BUILTIN, HIGH);
			delay(time);
			digitalWrite(LED_BUILTIN, LOW);
			noTone(BUZZER);
		}
		else {
			noTone(BUZZER);
			digitalWrite(LED_BUILTIN, LOW);
			delay(-time);
		}
}

// Char to Time
float char_to_time(char c) {
	float time = 0.0;
	switch (c)
	{
	case '.':
		time = t_unit * dit;
		break;
	case '_':
		time = t_unit * dah;
		break;
	case 'i':
		time = - t_unit * intra;
		break;
	case 'j':
		time = - t_unit * inter;
		break;
	case ' ':
		time = - t_unit * space;
		break;
	default:
		break;
	}
	// Return it (in miliseconds)
	return time;
}