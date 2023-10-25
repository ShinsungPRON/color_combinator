#define RA_PUMP 2
#define RB_PUMP 3
#define YA_PUMP 4
#define YB_PUMP 5
#define BA_PUMP 6
#define BB_PUMP 7
#define PA_PUMP 8
#define PB_PUMP 9

long R;
long Y;
long B;
long P;
char ch;

void setup() {
  Serial.begin(9600);
  Serial.println("Hi");
  pinMode(RA_PUMP, OUTPUT);
  pinMode(YA_PUMP, OUTPUT);
  pinMode(BA_PUMP, OUTPUT);
  pinMode(PA_PUMP, OUTPUT);

  pinMode(RB_PUMP, OUTPUT);
  pinMode(YB_PUMP, OUTPUT);
  pinMode(BB_PUMP, OUTPUT);
  pinMode(PB_PUMP, OUTPUT);
}

long readLock() {
  while (!Serial.available()) {
    delay(50);
  }

  long buf = Serial.parseInt();
  //  Serial.read(); // 개행 skip

  return buf;
}

void loop() {
  // put your main code here, to run repeatedly:
  while (true) {
    if (Serial.available()) {
      ch = Serial.read();  // begin 스킵
      //      Serial.read(); // 개행 skip

      if (ch != 'b') continue;

      delay(100);

      R = readLock();
      Serial.println(R);
      Y = readLock();
      Serial.println(Y);
      B = readLock();
      Serial.println(B);
      P = readLock();
      Serial.println(P);

      Serial.flush();


      digitalWrite(RA_PUMP, HIGH);
      digitalWrite(RB_PUMP, LOW);
      delay(R);
      digitalWrite(RA_PUMP, LOW);
      digitalWrite(RB_PUMP, LOW);

      digitalWrite(YA_PUMP, HIGH);
      digitalWrite(YB_PUMP, LOW);
      delay(Y);
      digitalWrite(YA_PUMP, LOW);
      digitalWrite(YB_PUMP, LOW);

      digitalWrite(BA_PUMP, HIGH);
      digitalWrite(BB_PUMP, LOW);
      delay(B);
      digitalWrite(BA_PUMP, LOW);
      digitalWrite(BB_PUMP, LOW);

      digitalWrite(PA_PUMP, HIGH);
      digitalWrite(PB_PUMP, LOW);
      delay(P);
      digitalWrite(PA_PUMP, LOW);
      digitalWrite(PB_PUMP, LOW);

      Serial.println(1);
    }
    delay(100);
  }
}
