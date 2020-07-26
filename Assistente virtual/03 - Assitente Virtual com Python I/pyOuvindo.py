'''
Instalei a versão do Python 3.7.7 com o PATH

Comandos que funcionaram:
pip install pipwin
pipwin install pyaudio

Esse não foi preciso usar:
python pip install python-pyaudio
'''

import speech_recognition as sr #Estou chamando o pacote speech_recognition com o apelido sr
import pyttsx3 #Serve para transformar um texto em voz, também executa qualquer arquivo mp3

engine = pyttsx3.init() #Ativa o pacote pyttsx3
r = sr.Recognizer()     #Ativa o reconhecimento da fala
mic = sr.Microphone()   #Habilita o microfone do PC

nome = input("Me informe o seu nome, por favor: ")

with mic as fonte: #Com o teu microfone ligado na fonte
    r.adjust_for_ambient_noise(fonte) #Faz o ajuste do reconhecimento da fala para o ruído do ambiente
    print("Fale alguma coisa: ")
    audio = r.listen(fonte) #Executa a fala, somente quando não for detectado ruídos
    print("Enviando para reconhecimento...")

    #Faz o tratamento das informações pertinentes ao usuário
    try: #Se tudo que está sendo executado estiver correto, executa os comandos abaixo
        text = r.recognize_google(audio, language="pt-BR") #Está sendo enviado para o Google o áudio na língua brasileira
        print("{}, você disse: {}".format(nome, text))
        engine.say("{}, você disse: {}".format(nome, text)) #Executa uma fala
        engine.runAndWait() #Roda o comando da fala e aguarda um tempo
        engine.stop() #Para o programa

        '''
        text = text.lower() #Manipulação de strings
        if text == "que horas são":
            print("LISO")
            engine.say("LISO")
            engine.runAndWait()
            engine.stop()
        '''

    except: #Senão mostra os possíveis erros para os comandos não terem sido executados
        print("Não entendi o que você falou!")
        engine.say("Não entendi o que você falou!")
        engine.runAndWait()
        engine.stop()