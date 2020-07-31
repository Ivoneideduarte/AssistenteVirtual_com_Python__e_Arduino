char letra;                 //Inicializa como string vazia
String frase = "";          //Inicializa vazia
bool fraseCompleta = false; //Inicializa em falso
String led = "desligado";   //O LED inicializa desligado
#define ledBlink 12

void setup()
{
  Serial.begin(115200);
}

void loop()
{
  if (fraseCompleta)
  {
    Serial.println("Frase tratada: " + frase); //Mostra na serial o texto escrito
    if (frase.startsWith("ligar"))
    { //Testa se uma String começa ou não com os caracteres de uma outra String
      if (led == "ligado")
      {
        Serial.println("O led já está " + led);
      }
      else
      {
        Serial.println("Ligando luz. \n");
        digitalWrite(ledBlink, HIGH);
        led = "ligado";
      }
    }
    else if (frase.startsWith("desligar"))
    {
      if (ledBlink == "desligado")
      {
        Serial.println("O led já está " + led);
      }
      else
      {
        Serial.println("Desligando luz. \n");
        digitalWrite(ledBlink, LOW);
        led = "desligado";
      }
    }
//    else if (frase.lastIndexOf("ligar"))
//    { //Localiza um caractere ou String dentro de outra String.
//      if (frase.lastIndexOf("lampada"))
//      {
//        Serial.println("Ligando a lampada. \n");
//        //Fogão = true; ligado
//        //eletrodomestico();
//      }
//    }
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
