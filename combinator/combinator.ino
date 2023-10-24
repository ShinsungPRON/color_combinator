#define R_PUMP 1
#define Y_PUMP 2
#define B_PUMP 3
#define P_PUMP 4

int R;
int Y;
int B;
int P;

void setup() {
  Serial.begin(9600);
  pinMode(R_PUMP, OUTPUT);
  pinMode(Y_PUMP, OUTPUT);
  pinMode(B_PUMP, OUTPUT);
  pinMode(P_PUMP, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available()) {
    Serial.readString();  // begin 스킵
    R = Serial.parseInt();
    G = Serial.parseInt();
    B = Serial.parseInt();
    P = Serial.parseInt();

    digitalWrite(R_PUMP, HIGH);
    delay(R);
    digitalWrite(R_PUMP, LOW);
    
    digitalWrite(Y_PUMP, HIGH);
    delay(Y);
    digitalWrite(Y_PUMP, LOW);

    digitalWrite(B_PUMP, HIGH);
    delay(B);
    digitalWrite(B_PUMP, LOW);

    digitalWrite(P_PUMP, HIGH);
    delay(P);
    digitalWrite(P_PUMP, LOW);

    Serial.write("done");
  }
}
