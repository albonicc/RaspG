#include <DHT.h>
#include <Wire.h>

int soil_hum = A0;
int pump = 10;// moisture sensor is connected with the analog pin A1 of the Arduino
int msvalue = 0; // moisture sensor value
int sensor_dht = 9;
int photo_res = A2;
int lum = 0;
int temp = 0, air_hum = 0;  
int data[4] = {0, 0, 0, 0};
int x = 0;
boolean flag = false;
char humAir[4];
char tempAir[4];
char humDirt[4];
char light[4];
char dataF[16];


DHT dht(sensor_dht, DHT11);

void setup() {
  
  Wire.begin(0x20);
  Wire.onRequest(sendData);
  Serial.begin(9600);
  dht.begin();
  pinMode(soil_hum, INPUT);
  pinMode(lum, INPUT);
  pinMode(pump, OUTPUT);
  
}


void sendData(){

  Wire.write(dataF);

}

void loop() 
{
  air_hum = dht.readHumidity();
  temp = dht.readTemperature();
  msvalue = analogRead(soil_hum);
  lum = analogRead(photo_res);

  itoa(air_hum, humAir, 10);
  itoa(temp, tempAir, 10);
  itoa(msvalue, humDirt, 10);
  itoa(lum, light, 10);

  sprintf(dataF, "%04s%04s%04s%04s",humAir,tempAir,humDirt,light);
  
  Serial.print("Humedad tierra: ");
  Serial.println(humDirt);
  Serial.print("Humedad aire: ");
  Serial.println(humAir);
  Serial.print("Temperatura: ");
  Serial.println(tempAir);
  Serial.print("Luminosidad: ");
  Serial.println(light);
  Serial.print("DATAF: ");
  Serial.println(dataF);
  Serial.println();
  
  
  if (msvalue >= 500) 
  { 
    digitalWrite(pump, HIGH);
    delay(200);
    digitalWrite(pump, LOW); 
  }
  delay(1000);   
}
