import speech_recognition as sr  # Estou chamando o pacote speech_recognition(reconhecimento de fala) com o apelido sr
import pyttsx3  # Responsável por executar o áudio

import serial
import threading
import time

conectado = False
desligarArduinoThread = False
mensagensRecebidas = 1
serialArduino = 0

# posso criar inputs para esses parâmetros
portaCOM = 'COM5'
velocidadeBaud = 115200

# Se isso for válido, entra aqui
try:
    # Comunicação com a serial
    serialArduino = serial.Serial(portaCOM, velocidadeBaud, timeout=0.2)
    print('Conectado!')

# Se não for válido, entra aqui
except:
    print('Verifique a porta serial do seu Arduino ou reconecte seu Arduino!')


def handle_data(data):
    global mensagensRecebidas

    print('Recebi ' + str(mensagensRecebidas) + ': ' + data)
    mensagensRecebidas += 1


# É necessario criar uma função pro Thread
def read_from_port(ser):
    global conectado, desligarArduinoThread

    while not conectado:
        conectado = True

        while True:
            reading = ser.readLine().decode()

            if reading != "":  # Leitura diferente de vazio
                handle_data(reading)

            if desligarArduinoThread:
                print('Desligando Arduino')
                break


def mensagem(msg):
    print('=' * 35)
    print(msg)
    print('=' * 35)


def comando_de_Voz(msg):
    engine.say(msg)  # Executa uma fala
    engine.runAndWait()  # Roda o comando da fala e aguarda um tempo
    engine.stop()  # Para o programa


def ajuste_ruido_ambiente(msg):
    global audio
    r.adjust_for_ambient_noise(fonte)  # Faz o ajuste do reconhecimento da fala para o ruído do ambiente
    comando_de_Voz(msg)
    audio = r.listen(fonte)  # Executa a fala, somente quando não for detectado ruídos
    print('Enviando para reconhecimento...')


lerSerialThread = threading.Thread(target=read_from_port, args=(serialArduino,))
lerSerialThread.start()

print('Preparando o Arduino')
time.sleep(2)
print('Arduino pronto!')

engine = pyttsx3.init()  # Ativa o pacote pyttsx3
r = sr.Recognizer()  # Ativa o reconhecimento de fala e áudio
mic = sr.Microphone()  # Habilita o microfone do PC
audio = 0

mensagem('ASSISTENTE VIRTUAL COM PYTHON')

with mic as fonte:
    print('Para iniciarmos uma conversa, me chame pelo meu nome: Python!')
    ajuste_ruido_ambiente('Para iniciarmos uma conversa, me chame pelo meu nome: Python!')

    try:
        text = r.recognize_google(audio, language="pt-BR")
        comando_de_Voz(f'Você disse {text}, já que está correto, podemos iniciar')

        text = text.lower()
        while text == "python":
            print('Olá, qual o seu nome?')
            ajuste_ruido_ambiente('Olá, qual o seu nome?')

            try:
                text2 = r.recognize_google(audio, language="pt-BR")
                print(f'É um prazer conhecê-la, {text2}')
                comando_de_Voz(f'É um prazer conhecê-la, {text2}')

                '''O Assistente está habilitado para o modo conversa a partir daqui'''
                text = text.lower()
                while text == "python":
                    text3 = r.recognize_google(audio, language="pt-BR")
                    mensagem(f'Em que posso ajudá-la, {text2}?')
                    ajuste_ruido_ambiente(f'Em que posso ajudá-la, {text2}?')

                    try:
                        text3 = r.recognize_google(audio, language="pt-BR")

                        text3 = text3.lower()
                        if text3 == 'ligar led':
                            print('Pronto, está ligado!')
                            comando_de_Voz('Pronto, está ligado!')
                            serialArduino.write('ligar led\n'.encode())
                            time.sleep(2)
                        elif text3 == 'desligar led':
                            print('Pronto, está desligado!')
                            comando_de_Voz('Pronto, está desligado!')
                            serialArduino.write('desligar led\n'.encode())
                            time.sleep(2)
                        elif text3 == 'dispensado':
                            text = text3
                            print('Certo, até mais!')
                            comando_de_Voz('Certo, até mais!')
                            print("")

                    except:
                        print('Desculpe, não entendi o que você disse!')
                        comando_de_Voz('Desculpe, não entendi o que você disse!')
            except:
                print('Desculpe, não entendi o que você disse!')
                comando_de_Voz('Desculpe, não entendi o que você disse!')
    except:
        print('você errou o meu nome, por isso, não podemos conversar')
        comando_de_Voz('você errou o meu nome, por isso, não podemos conversar')