#include<Wire.h>
const int MPU=0x68; // I2C address of the MPU-6050
int16_t AcX,AcY,AcZ,Tmp,GyX,GyY,GyZ;
void setup(){
 Wire.begin();
 Wire.beginTransmission(MPU);
 Wire.write(0x6B); // PWR_MGMT_1 register
 Wire.write(0); // set to zero (wakes up the MPU-6050)
 Wire.endTransmission(true);
 Serial.begin(9600);
 pinMode(LED_BUILTIN, OUTPUT);

 //Keyboard.begin();
}
void loop(){
 Wire.beginTransmission(MPU);
 Wire.write(0x3B); // starting with register 0x3B (ACCEL_XOUT_H)
 Wire.endTransmission(false);
 Wire.requestFrom(MPU,14,true); // request a total of 14 registers
 AcX=Wire.read()<<8|Wire.read(); // 0x3B (ACCEL_XOUT_H) & 0x3C (ACCEL_XOUT_L)
 AcY=Wire.read()<<8|Wire.read();
 AcZ=Wire.read()<<8|Wire.read();
 

// Serial.print(AcX);
// Serial.print(" ");
 Serial.print(AcY);
 Serial.println(" ");
// Serial.print(AcZ);
// Serial.println(" ");
 
 


 
 delay(100);
 //Keyboard.write(65)
}
