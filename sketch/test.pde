// test temperature + dust pm10 sensor

#include <WaspSensorCities.h>

float value;
float temperature;

void setup()
{
  USB.ON();
  USB.println(F("start"));
  delay(1000);

  SensorCities.ON();
  SensorCities.setSensorMode(SENS_ON, SENS_CITIES_DUST);
  SensorCities.setSensorMode(SENS_ON, SENS_CITIES_TEMPERATURE);
  
}
 
void loop()
{
  value = SensorCities.readValue(SENS_CITIES_DUST);
  temperature = SensorCities.readValue(SENS_CITIES_TEMPERATURE);

  USB.print(F("Particles: "));
  USB.print(value);
  USB.println(F("mg/m3"));
  
  USB.print(F("Temperature: "));
  USB.print(temperature);
  USB.println(F(" C"));
  
  delay(1000);
}