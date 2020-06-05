int msensor = A0;
int pump = 10;// moisture sensor is connected with the analog pin A1 of the Arduino
int msvalue = 0; // moisture sensor value  
boolean flag = false;
void setup() {
  Serial.begin(9600);
  pinMode(msensor, INPUT);
  pinMode(pump, OUTPUT);
  
}
 
void loop() 
{
  msvalue = analogRead(msensor);
  Serial.println(msvalue);
  
  if ( (msvalue >= 500  ) && ( flag == false ) )
  { 
    flag = true;
    digitalWrite(pump, HIGH); 
   }
 
  if ( (msvalue <= 300  ) && ( flag == true ) )
  { 
    flag = false;
    digitalWrite(pump, LOW);
  } 
       
}
