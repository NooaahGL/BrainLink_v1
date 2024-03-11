// Arduino Brain Library - Brain Serial Test

// Description: Grabs brain data from the serial RX pin and sends CSV out over the TX pin (Half duplex.)

#include <Brain.h>

// Set up the brain parser, pass it the hardware serial object you want to listen on.
Brain brain(Serial);

void setup() {
  // put your setup code here, to run once:
  // Start the hardware serial.
    Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
    // Expect packets about once per second.
    // The .readCSV() function returns a string (well, char*) listing the most recent brain data, in the following format:
    // "signal strength, attention, meditation, delta, theta, low alpha, high alpha, low beta, high beta, low gamma, high gamma"    
    if (brain.update()) {
        Serial.println(brain.readErrors());
        Serial.println(brain.readCSV());
    }

    // Si el dispositivo Brain envía datos a una velocidad diferente a la que tu Arduino está leyendo, 
    // podrías perder algunos datos. Asegúrate de que la velocidad del puerto serie coincida con la configuración 
    // del dispositivo Brain.

}
