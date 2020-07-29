import speech_recognition as sr
import pyttsx3


# Funções
def mensagem(msg):
    print('=' * 30)
    print(msg)
    print('=' * 30)


def comando_de_Voz(msg):
    engine.say(msg)
    engine.runAndWait()
    engine.stop()


def ajuste_ruido_ambiente(msg):
    global audio
    r.adjust_for_ambient_noise(fonte)
    comando_de_Voz(msg)
    audio = r.listen(fonte)
    print('Enviando para reconhecimento...')


engine = pyttsx3.init()
r = sr.Recognizer()
mic = sr.Microphone()

mensagem('ASSISTENTE VIRTUAL COM PYTHON')
nome = input('\nQual o seu nome? ')

with mic as fonte:
    print('Me chame pelo meu nome!')
    ajuste_ruido_ambiente('Me chame pelo meu nome!')

    try:
        text = r.recognize_google(audio, language="pt-BR")
        print(f'{nome}, você disse: {text}')
        comando_de_Voz(f'{nome}, você disse: {text}')

        text = text.lower()
        if text == "python":
            print(f'Seja bem-vinda, {nome}')
            comando_de_Voz(f'Seja bem-vinda, {nome}')

            while True:
                mensagem('Em que posso te ajudar? ')
                ajuste_ruido_ambiente('Em que posso te ajudar?')

                try:
                    text = r.recognize_google(audio, language="pt-BR")
                    print(text)
                    comando_de_Voz(text)

                    text = text.lower()
                    if text == 'dispensado':
                        print('Certo, até mais.')
                        comando_de_Voz('Certo, até mais.')
                        break
                except:
                    print('Não entendi o que você falou!')
                    comando_de_Voz('Não entendi o que você falou!')
        else:
            print('Você errou o meu nome!')
            comando_de_Voz('Você errou o meu nome!')

    except:
        print('Não entendi o que você falou!')
        comando_de_Voz('Não entendi o que você falou!')