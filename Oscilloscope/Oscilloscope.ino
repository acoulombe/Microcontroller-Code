int osc = A0;

void setup() {
  // put your setup code here, to run once:
  pinMode(osc, INPUT);

  Serial.begin(115200);
}

void loop() {
  // put your main code here, to run repeatedly:
  int data = analogRead(osc);
  Serial.println(data);
}
