//Beverage machine
#include <LiquidCrystal.h>
//const int rs = 12, en = 11, d4 = 7, d5 = 8, d6 = 9, d7 = 10;
const int rs = 12, en = 11, d4 = 10, d5 = 9, d6 = 8, d7 = 7;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);
int hits=0;
int max_val;
void setup() {
  // put your setup code here, to run once:
  pinMode(A0, INPUT);
  lcd.begin(16, 2);
  lcd.clear();
  lcd.print("Initializing");
  delay(1000);
 // Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly
  max_val=1023;
  lcd.clear();
  lcd.setCursor(0,0);
  lcd.print("Score: ");
  lcd.setCursor(8,0);
  lcd.print("Hits:");
  while(max_val>810){
    for(int i=0;i<100;i++){
      int value= analogRead(A0);
     // Serial.println(value);
      if(value<max_val){
        max_val=value;
      }
      delay(20);
    }
  }
  float Score=62.5*(0.8-(float)max_val/1023);//100-((float)max_val/1023*100);
  //Serial.println(Score);
  if(Score>0.5){
    lcd.setCursor(0,1);
    lcd.print(Score);
    hits++;
    lcd.setCursor(8,1);
    lcd.print(hits);
  }
  delay(10000);
}
