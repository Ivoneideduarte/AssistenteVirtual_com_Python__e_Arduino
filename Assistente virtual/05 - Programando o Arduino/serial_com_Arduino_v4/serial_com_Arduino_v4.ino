char letra; //Inicializa como string vazia
String frase = "";
bool fraseCompleta = false;
String led = "desligado";

void setup()
{
  Serial.begin(9600);
}

void loop()
{
  if (fraseCompleta)
  {
    Serial.println("Frase tratada: " + frase);
    if (frase.startsWith("ligar"))
    {
      if (led == "ligado")
      {
        Serial.println("O led já está " + led);
      }
      else
      {
        Serial.println("Ligando luz. \n");
        led = "ligado";
      }
    }
    else if (frase.startsWith("desligar"))
    {
      if (led == "desligado")
      {
        Serial.println("O led já está " + led);
      }
      else
      {
        Serial.println("Desligando luz. \n");
        led = "desligado";
      }
    }
    else if (frase.lastIndexOf("ligar") >= 0)
    {
      if (frase.lastIndexOf("lampada") >= 0)
      {
        Serial.println("Ligando a lampada. \n");
        //Fogão = true; ligado
        //eletrodomestico();

      }
    }
    else Serial.println("Não reconheço este comando!");

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
      //      Serial.println("Tudo minusculo: " + frase);
      //      frase.toLowerCase(); //Converte para letra minuscula
      //      Serial.println("Tudo maiusculo: " + frase);
      //      frase.toUpperCase();

      fraseCompleta = true;
    }
    else frase += letra;
  }
}

//void eletrodomestico()
//{
//  if (fogao) {
//    estadoFogao = !estadoFogao;
//    digitalWrite(fogao, estadoFogao);
//  }
//  else if (geladeira)
//  {
//
//  }
//}
//
//void lampadas()
//{
//
//}
//
//void piscina()
//{
//
//}
