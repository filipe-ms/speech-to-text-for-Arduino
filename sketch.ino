/*                 *
****** C code ******
*                  */

void setup() {
  // Arduino setup code:
  Serial.begin(9600);
}

void loop() {
  // Arduino loop code:
  
  if(Serial.available()!=0) { // Checks if the serial port is available.
    String commandFromPython = Serial.readString();
    const char* commandToCharArray = commandFromPython.c_str(); // Converting the String read from COM to a char array.
    
    if(strcmp(commandToCharArray, "YOUR_STRING/0")){ 
      // If the string read from the COM port equals to "YOUR_STRING/0", do this:
    
    }
  }
}
