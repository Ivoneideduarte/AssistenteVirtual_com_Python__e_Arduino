'''Instalar pelo prompt: pip install pyttsx3'''
import pyttsx3 #Serve para transformar um texto em voz, também executa qualquer arquivo mp3

'''
text = input('Escreva o que você quer que o Python fale: ')

engine = pyttsx3.init() #Inicialização do pacote

engine.say('Sua frase: ' + text) #Fale essa frase
engine.runAndWait() #Rode e aguarde
engine.stop() #Parar
'''

'''
- Importa o pacote
- Inicializa o pacote
- Diz o que quer que o pacote execute
- Chama o método para rodar e aguardar
- E pede para parar
'''
#Esse programa pode ser usado como recurso de segurança residencial
text = input('Me informe o seu nome, por favor? ')

engine = pyttsx3.init() #Inicialização do pacote
#Para esse caso a concatenação com + é importante
#engine.say('Prazer ' + text)
engine.say('Seu acesso foi liberado, {}!'.format(text)) #Executa uma fala
engine.runAndWait() #Roda o comando da fala e aguarda um tempo
engine.stop() #Para o programa

