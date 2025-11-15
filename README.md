Smart Band Prototype

An energy-efficient, multi-sensor wearable device designed for real-time health monitoring using IoT. This smart band integrates biomedical sensors with wireless communication, solar-assisted power management, and cloud dashboards for remote tracking.

Overview

The Smart Band Prototype is a compact health-monitoring wearable built using Raspberry Pi Pico W, integrating vital biomedical sensors to measure:

Heart Rate

SpO₂

Body Temperature

ECG

Motion & Orientation

It sends real-time health data to a mobile/online dashboard using Blynk IoT.


Features

 Multi-sensor monitoring (HR, SpO₂, ECG, Temp, Motion)

 Wireless IoT connectivity using Pico W

 Solar-assisted power system for extended battery life

 Modular firmware for easy debugging & expansion

 Real-time dashboard on Blynk IoT

 Low-power system design using Li-ion battery + TP4056

 Compact wearable form-factor prototype

 Secure cloud communication

 
 Hardware Components
Microcontroller

Raspberry Pi Pico W (WiFi-enabled)

Sensors

MAX30100 — SpO₂ + Heart Rate

AD8232 — ECG signal monitoring

LM35 — Body temperature sensor

MPU6050 — Accelerometer + Gyroscope

Power System

Li-ion Battery (3.7V)

TP4056 Charge Controller

Solar Panel Module

Voltage Regulation (Buck converter if needed)



Software / IoT

Blynk IoT Platform

Real-time graphs & widgets

Cloud database & device monitoring

Alerts & notifications (optional)


System Architecture
[Sensors] → [Raspberry Pi Pico W] → [WiFi] → [Blynk IoT Cloud] → [Mobile App / Dashboard]


How It Works

The Raspberry Pi Pico W continuously reads data from all sensors.

Vital signs are processed using lightweight algorithms.

Data is pushed to Blynk Cloud via WiFi.

The mobile app displays:

Live graphs

ECG waveform

Alerts for abnormal readings


Blynk Dashboard Includes

Heart Rate Graph

SpO₂ Chart

Temperature Gauge

ECG Live Plot

Motion Vector

Device Online/Offline Indicator



Testing Performed

Sensor accuracy cross-checked with medical-grade devices

WiFi stability tested

Solar charging validated

Prototype tested on wrist model



Future Enhancements

AI/ML-based anomaly detection

Sleep tracking

Fall-detection alerts

GPS module

OLED/AMOLED display

Waterproof casing

BLE + MQTT support




Author

Vibha
Smart Band Prototype, 2025
 IoT • Embedded Systems • Prototyping • Health Tech