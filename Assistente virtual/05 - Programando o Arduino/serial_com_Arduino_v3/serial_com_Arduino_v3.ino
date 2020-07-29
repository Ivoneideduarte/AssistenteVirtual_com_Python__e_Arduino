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
    Serial.println("Frase tratada: " + frase);
    if (frase == "ligar")
    {
      Serial.println("Ligando lampada. \n");
    }
    else if (frase == "desligar")
    {
      Serial.println("Desligando lampada. \n");
    }
    else Serial.println("Não tenho esse comando em meus registros. \n");
    
    frase = "";
    fraseCompleta = false;
  }
}

void serialEvent()
{
  while (Serial.available() > 0)
  {
    letra = char(Serial.read());
    if (letra == char(10))
    {
      Serial.println("Tudo minusculo: " + frase);
      frase.toLowerCase(); //Converte para letra minuscula
      Serial.println("Tudo maiusculo: " + frase);
      frase.toUpperCase();
      
      fraseCompleta = true;
    }
    else frase += letra;
  }
}
