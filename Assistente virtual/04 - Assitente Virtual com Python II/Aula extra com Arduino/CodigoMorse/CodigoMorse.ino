/*#include <Arduino.h> //Estudar essa biblioteca

  byte led = 13;
  bool LIGADO = 1, DESLIGADO = 0;

  void setup()
  {

  }

  void loop()
  {
  digitalWrite(led, LIGADO);
  }

  void digitalwrite(byte porta, bool estado) //Dois argumentos
  {

  }*/
  
byte led = 10;

void setup()
{
  pinMode(led, OUTPUT);
}

void loop()
{
  //Letra 'S' em código Morse
  for (int x = 0; x < 3; x++)
  {
    digitalWrite(led, HIGH);
    delay(150);
    digitalWrite(led, LOW);
    delay(100);
  }
  //Letra 'O' em código Morse
  for (int x = 0; x < 3; x++)
  {
    digitalWrite(led, HIGH);
    delay(400);
    digitalWrite(led, LOW);
    delay(100);
  }
  //Letra 'S' em código Morse
  for (int x = 0; x < 3; x++)
  {
    digitalWrite(led, HIGH);
    delay(150);
    digitalWrite(led, LOW);
    delay(100);
  }
  delay(5000);
}
