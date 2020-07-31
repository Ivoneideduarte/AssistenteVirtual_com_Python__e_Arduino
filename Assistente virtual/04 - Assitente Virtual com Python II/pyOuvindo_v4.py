import speech_recognition as sr  # Estou chamando o pacote speech_recognition(reconhecimento de fala) com o apelido sr
import pyttsx3  # Responsável por executar o áudio

# Funções
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
                        if text3 == "como vai você":
                            print('Estou bem, e você?')
                            comando_de_Voz('Estou bem, e você?')
                        else:
                            print(text3 + " ")
                            comando_de_Voz(text3 + " ")

                    except:
                        print('Desculpe, não entendi o que você disse!')
                        comando_de_Voz('Desculpe, não entendi o que você disse!')
            except:
                print('Desculpe, não entendi o que você disse!')
                comando_de_Voz('Desculpe, não entendi o que você disse!')
    except:
        print('você errou o meu nome, por isso, não podemos conversar')
        comando_de_Voz('você errou o meu nome, por isso, não podemos conversar')
