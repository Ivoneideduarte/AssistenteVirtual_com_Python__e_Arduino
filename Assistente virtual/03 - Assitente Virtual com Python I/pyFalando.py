'''Instalar pelo prompt: pip install pyttsx3'''
import pyttsx3

'''text = input('Escreva o que você quer que o Python fale: ')

engine = pyttsx3.init() #Inicialização do pacote

engine.say('Sua frase: ' + text) #Fale essa frase
engine.runAndWait() #Rode e aguarde
engine.stop() #Parar'''

text = input('Qual o seu nome? ')

engine = pyttsx3.init() #Inicialização do pacote

engine.say('Prazer ' + text) #Fale essa frase
engine.runAndWait() #Rode e aguarde
engine.stop() #Parar