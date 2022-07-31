volatile int ledstate = LOW;

int ledpin = 4;
int pidpin = 2;

void setup()
{
    pinMode(ledpin,OUTPUT);
    pinMode(pidpin,INPUT);
    attachInterrupt(digitalPinToInterrupt(pidpin),p_ISR,RISING);
    Serial.begin(9600);
}

void loop()
{
    if(ledstate ==HIGH)
    {
        delay(100);
        ledstate = !ledstate;
        digitalWrite(ledpin,ledstate);
    }
}

void p_ISR()
{
    ledstate = !ledstate;
    Serial.print(ledstate);
    Serial.print("\n");
    digitalWrite(ledpin,ledstate);
}
