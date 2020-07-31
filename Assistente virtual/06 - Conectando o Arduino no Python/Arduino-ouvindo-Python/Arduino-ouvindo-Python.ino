String inputString = "";
bool StringComplete = false;

void setup()
{
  Serial.begin(115200);
  inputString.reserve(200);

  pinMode(LED_BUILTIN, OUTPUT);
}

void loop()
{
  if (StringComplete)
  {
    Serial.print("Assistente Virtual Arduino falando: ");
    Serial.print(inputString);
  }
  if (inputString.startsWith("ligar luzes"))
  {
    digitalWrite(LED_BUILTIN, HIGH);
  }
  if (inputString.startsWith("desligar luzes"))
  {
    digitalWrite(LED_BUILTIN, LOW);
  }
  inputString = "";
  StringComplete = false;
}

void serialEvent()
{
  while (Serial.available())
  {
    char inChar = (char)Serial.read();
    inputString += inChar;

    if (inChar == '\n')
    {
      StringComplete = true;
    }
  }
}
