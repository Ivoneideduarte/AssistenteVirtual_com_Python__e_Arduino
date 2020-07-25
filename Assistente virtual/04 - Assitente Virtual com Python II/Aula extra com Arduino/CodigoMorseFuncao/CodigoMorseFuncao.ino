//byte led = 10;
int y = 0;

void setup()
{
  pinMode(10, OUTPUT);
  pinMode(13, OUTPUT);
  Serial.begin(9600);
}

void loop()
{
  piscaLed(150, 100, 10, 3); //Argumentos
  Serial.println("Escrevendo S.");
  piscaLed(400, 100, 10, 3);
  Serial.println("0.");
  piscaLed(150, 100, 10, 3);
  Serial.println("S");
  Serial.println("Enviado S.O.S "+String(y)+" vez."); //Concatenando variáveis

  /*piscaLed(150, 100, 13, 10);
  Serial.println("Escrevendo S.");
  piscaLed(400, 100, 13, 10);
  Serial.println("0.");
  piscaLed(150, 100, 13, 10);
  Serial.println("S");
  Serial.println("Enviado S.O.S");*/
}
//Void é uma função vazia, não retorna nada
int piscaLed(int tempLig, int tempDesl, byte porta, int qtd) //Argumentos
{
  for (int x = 0; x < qtd; x++)
  {
    digitalWrite(porta, HIGH);
    delay(tempLig);
    digitalWrite(porta, LOW);
    delay(tempDesl);
  }
  
  y++;
  return y; //Retorna o valor do incremento do y
}
