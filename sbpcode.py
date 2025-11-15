
#define BLYNK_TEMPLATE_ID "TMPL3JjJxegTQ"
#define BLYNK_TEMPLATE_NAME "smart watch prototype"
#define BLYNK_AUTH_TOKEN  "5J8Hmff21z_Oh67eo6FJKsxzmCxarWPj"

#include <WiFi.h>
#include <BlynkSimpleWifi.h>
#include <Wire.h>
#include "MAX30100_PulseOximeter.h"

// Enter your WiFi credentials
char ssid[] = "vibha";
char pass[] = "vibha2105";

// Blynk auth token
char auth[] = BLYNK_AUTH_TOKEN;

// LM35 connected to ADC pin
#define LM35_PIN 26   // GPIO 26 = ADC0 on Pico W

// MAX30100 object
PulseOximeter pox;

// Timer for Blynk
BlynkTimer timer;

// For MAX30100 HR/SpO2
uint32_t tsLastReport = 0;

// Function to send LM35 data
void sendSensorData() {
  // LM35 → 10mV/°C
  int adcValue = analogRead(LM35_PIN);
  float voltage = adcValue * (3.3 / 4095.0); // 12-bit ADC
  float temperatureC = voltage * 100.0;      // °C

  Blynk.virtualWrite(V0, temperatureC);  // V0 = Temperature
  Serial.print("Temp: ");
  Serial.println(temperatureC);
}

// Callback for heart rate detection
void onBeatDetected() {
  Serial.println("Beat!");
}

void setup() {
  Serial.begin(115200);

  // WiFi + Blynk connection
  Blynk.begin(auth, ssid, pass);

  // LM35 pin as input
  pinMode(LM35_PIN, INPUT);

  // MAX30100 initialization
  if (!pox.begin()) {
    Serial.println("FAILED to init MAX30100");
    for(;;);
  } else {
    Serial.println("MAX30100 ready");
  }
  pox.setOnBeatDetectedCallback(onBeatDetected);

  // Timer: send temp every 2s
  timer.setInterval(2000L, sendSensorData);
}

void loop() {
  Blynk.run();
  timer.run();

  // Update MAX30100
  pox.update();

  // Every 2s send HR + SpO2
  if (millis() - tsLastReport > 2000) {
    float hr = pox.getHeartRate();
    float spo2 = pox.getSpO2();

    Serial.print("Heart Rate: ");
    Serial.print(hr);
    Serial.print(" bpm | SpO2: ");
    Serial.print(spo2);
    Serial.println(" %");

    Blynk.virtualWrite(V1, hr);    // V1 = Heart Rate
    Blynk.virtualWrite(V2, spo2);  // V2 = SpO2

    tsLastReport = millis();
  }
}