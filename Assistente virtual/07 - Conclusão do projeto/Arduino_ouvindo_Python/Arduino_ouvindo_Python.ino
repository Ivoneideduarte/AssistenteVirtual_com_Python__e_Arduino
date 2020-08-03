char letra;                 //Inicializa como string vazia
String frase = "";          //Inicializa vazia
bool fraseCompleta = false; //Inicializa em falso
String luz = "desligado";
#define rele_luz 8

void setup()
{
  pinMode(rele_luz, OUTPUT);
  Serial.begin(115200);
}

void loop()
{
  if (fraseCompleta)
  {
    Serial.println("Frase tratada: " + frase); //Mostra na serial o texto escrito
    if (frase.startsWith("ligar luz"))
    { //Testa se uma String começa ou não com os caracteres de uma outra String
      if (luz == "ligado")
      {
        Serial.println("A luz já está " + luz);
      }
      else
      {
        Serial.println("Ligando a luz. \n");
        digitalWrite(rele_luz, HIGH);
        luz = "ligado";
      }
    }
    else if (frase.startsWith("desligar luz"))
    {
      if (luz == "desligado")
      {
        Serial.println("A lâmpada já está " + luz);
      }
      else
      {
        Serial.println("Desligando lampâda. \n");
        digitalWrite(rele_luz, LOW);
        luz = "desligado";
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
