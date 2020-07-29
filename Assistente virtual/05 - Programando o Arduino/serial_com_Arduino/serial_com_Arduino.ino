char letra; //Inicializa como string vazia
String frase = "";

void setup()
{
  Serial.begin(9600);
}

void loop()
{
  if (Serial.available() > 0)
  { //Faz a leitura da porta serial
    letra = char(Serial.read());
    frase += letra;
    if (letra == char(10))
    {
      Serial.println("Você disse: " + frase);
      Serial.print("\n");
      delay(50);
      frase = "";
    }
    else frase += letra;
  }
}
