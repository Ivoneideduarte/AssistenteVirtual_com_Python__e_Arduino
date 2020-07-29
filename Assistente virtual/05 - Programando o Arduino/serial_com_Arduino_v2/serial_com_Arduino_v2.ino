char letra; //Inicializa como string vazia
String frase = "";
bool fraseCompleta = false;

void setup()
{
  Serial.begin(9600);
}

void loop()
{
  if (fraseCompleta)
  {
    Serial.println("Você disse: " + frase);
    frase = "";
    fraseCompleta = false;
  }
}

void serialEvent()
{
  while (Serial.available() > 0)
  {
    letra = char(Serial.read());
    if (letra == '.')
    {
      fraseCompleta = true;
    }
    else frase += letra;
  }
}
