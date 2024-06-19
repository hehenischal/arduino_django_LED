void setup() {
  Serial.begin(9600);
  
  // Initialize the built-in LED pin as an output
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  // Check if data is available to read
  if (Serial.available() > 0) {
    // Read the incoming string until newline character
    String command = Serial.readStringUntil('\n');
    
    // Remove any trailing whitespace characters (like \r or \n)
    command.trim();
    
    // Check the command and perform the appropriate action
    if (command == "lightOn") {
      digitalWrite(LED_BUILTIN, HIGH);  // Turn the LED on
      Serial.println("LED is ON");
    } else if (command == "lightOff") {
      digitalWrite(LED_BUILTIN, LOW);   // Turn the LED off
      Serial.println("LED is OFF");
    } else {
      Serial.println("Unknown command");
    }
  }
}
