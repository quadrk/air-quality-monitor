// Ver 0.1.0

#include "libraries/WIFI/WaspWIFI.h"
#include "libraries/SensorCities/WaspSensorCities.h"

WaspWIFI wifi;
WaspSensorCities sensorCities;

void setup() {
  // Initialize serial communication
  USB.ON();
  USB.println(F("Communication started."));

  sensorCities.ON();
  sensorCities.setSensorMode(SENS_ON, SENS_CITIES_TEMPERATURE);


  // Power on the WiFi module
  if (wifi.ON(SOCKET0)) {
    USB.println(F("WiFi module is powered on."));
  } else {
    USB.println(F("Failed to power on WiFi module."));
    return;
  }

    // WiFi parameters
    wifi.setESSID(""); // SSID
    wifi.setAuthKey(WPA2, ""); // Password
    wifi.setIp("192.168.1.100");
    wifi.setNetmask("255.255.255.0");
    wifi.setGW("192.168.1.1");

    //wifi.storeData(); // Save configuration
    //wifi.reset();     // Reboot the module

    // Connect to the WiFi network
    if (wifi.join("fish")) {
        USB.println(F("Connected to WiFi network."));
    } else {
        USB.println(F("Failed to connect to WiFi network."));
        return;
    }
}

void loop() {
    float temperature = getTemperature();
    sendTemperature(temperature);
    delay(3000);
}

float getTemperature() {
  float temperature = sensorCities.readValue(SENS_CITIES_TEMPERATURE);
  USB.print("Catched temperature: ");
  USB.println(temperature);
  return temperature;
}

void sendTemperature(float temperature) {
    char tempStr[10]; 
    dtostrf(temperature, 5, 2, tempStr);

    char jsonBody[100];
    snprintf(jsonBody, sizeof(jsonBody), "{\"temperature\": %s}", tempStr);
    int contentLength = strlen(jsonBody);

    char request[300];
    snprintf(request, sizeof(request),
             "POST /temperature HTTP/1.1\r\n"
             "Host: 192.168.100.20\r\n"
             "Content-Type: application/json\r\n"
             "Content-Length: %d\r\n\r\n"
             "%s",
             contentLength, jsonBody);

    if (wifi.setTCPclient("192.168.100.20", 8000, 12345)) {
        USB.println(F("TCP connection opened."));
        wifi.send(request);
        USB.println(F("Temperature data sent: "));
        USB.println(jsonBody);
        wifi.close();
    } else {
        USB.println(F("Failed to open TCP connection."));
    }
}
