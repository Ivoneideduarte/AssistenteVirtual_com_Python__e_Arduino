char letra;                 //Inicializa como string vazia
String frase = "";          //Inicializa vazia
bool fraseCompleta = false; //Inicializa em falso
String luzQuarto = "desligado";
String luzSala = "desligado";
String luzBanheiro = "desligado";
String luzEscritorio = "desligado";
#define luz_Quarto 2
#define luz_Sala 3
#define luz_Banheiro 4 

void setup()
{
  pinMode(luz_Quarto, OUTPUT);
  pinMode(luz_Sala, OUTPUT);
  pinMode(luz_Banheiro, OUTPUT);
  Serial.begin(115200);
}

void loop()
{
  if (fraseCompleta)
  {
    Serial.println("Frase tratada: " + frase); //Mostra na serial o texto escrito
    if (frase.startsWith("ligar luz do quarto"))
    { //Testa se uma String começa ou não com os caracteres de uma outra String
      if (luzQuarto == "ligado")
      {
        Serial.println("A luz do quarto já está " + luzQuarto);
      }
      else
      {
        Serial.println("Ligando luz do quarto. \n");
        digitalWrite(luz_Quarto, HIGH);
        luzQuarto = "ligado";
      }
    }
    else if (frase.startsWith("desligar luz do quarto"))
    {
      if (luzQuarto == "desligado")
      {
        Serial.println("A luz do quarto já está " + luzQuarto);
      }
      else
      {
        Serial.println("Desligando luz do quarto. \n");
        digitalWrite(luz_Quarto, LOW);
        luzQuarto = "desligado";
      }
    }

    else if (frase.startsWith("ligar luz da sala"))
    { //Testa se uma String começa ou não com os caracteres de uma outra String
      if (luzSala == "ligado")
      {
        Serial.println("A luz da sala já está " + luzSala);
      }
      else
      {
        Serial.println("Ligando luz da sala. \n");
        digitalWrite(luz_Sala, HIGH);
        luzSala = "ligado";
      }
    }
    else if (frase.startsWith("desligar luz da sala"))
    {
      if (luzSala == "desligado")
      {
        Serial.println("A luz da sala já está " + luzSala);
      }
      else
      {
        Serial.println("Desligando luz da sala. \n");
        digitalWrite(luz_Sala, LOW);
        luzSala = "desligado";
      }
    }

    else if (frase.startsWith("ligar luz do banheiro"))
    { //Testa se uma String começa ou não com os caracteres de uma outra String
      if (luzBanheiro == "ligado")
      {
        Serial.println("A luz do banheiro já está " + luzBanheiro);
      }
      else
      {
        Serial.println("Ligando luz do banheiro. \n");
        digitalWrite(luz_Banheiro, HIGH);
        luzBanheiro = "ligado";
      }
    }
    else if (frase.startsWith("desligar luz do banheiro"))
    {
      if (luzBanheiro == "desligado")
      {
        Serial.println("A luz do banheiro já está " + luzBanheiro);
      }
      else
      {
        Serial.println("Desligando luz do banheiro. \n");
        digitalWrite(luz_Banheiro, LOW);
        luzBanheiro = "desligado";
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
