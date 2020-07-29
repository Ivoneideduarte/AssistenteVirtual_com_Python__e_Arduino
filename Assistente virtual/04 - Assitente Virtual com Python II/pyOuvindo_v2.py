import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()
r = sr.Recognizer()
mic = sr.Microphone()

nome = input('Qual o seu nome? ')

with mic as fonte:
    r.adjust_for_ambient_noise(fonte)
    print('Me chame pelo meu nome!')
    engine.say('Me chame pelo meu nome!')
    engine.runAndWait()
    engine.stop()
    audio = r.listen(fonte)
    print('Enviando para reconhecimento...')

    try:
        text = r.recognize_google(audio, language="pt-BR")
        print("{}, você disse: {}".format(nome, text))
        engine.say(f'{nome}, você disse: {text}')
        engine.runAndWait()
        engine.stop()

        if text == "Python":
            print(f'Seja bem-vinda, {nome}')
            engine.say(f'Seja bem-vinda, {nome}')
            engine.runAndWait()
            engine.stop()

            while True:
                r.adjust_for_ambient_noise(fonte)
                print('=' * 70)
                print('Em que posso te ajudar? ')
                engine.say('Em que posso te ajudar? ')
                engine.runAndWait()
                engine.stop()
                audio = r.listen(fonte)
                print('Enviando para reconhecimento...')

                try:
                    text = r.recognize_google(audio, language="pt-BR")
                    print(text)
                    engine.say(text)
                    engine.runAndWait()
                    engine.stop()

                    text = text.lower()
                    if text == 'dispensado':
                        print('Certo, até mais.')
                        engine.say('Certo, até mais.')
                        engine.runAndWait()
                        engine.stop()
                        break
                except:
                    print('Não entendi o que você falou!')
                    engine.say('Não entendi o que você falou!')
                    engine.runAndWait()
                    engine.stop()
        else:
            print('Você errou o meu nome!')
            engine.say('Você errou o meu nome!')
            engine.runAndWait()
            engine.stop()

    except:
        print('Não entendi o que você falou!')
        engine.say('Não entendi o que você falou!')
        engine.runAndWait()
        engine.stop()

'''Criar funções para esses parametros
engine.say('Você errou o meu nome, tente novamente!')
engine.runAndWait()
engine.stop()'''