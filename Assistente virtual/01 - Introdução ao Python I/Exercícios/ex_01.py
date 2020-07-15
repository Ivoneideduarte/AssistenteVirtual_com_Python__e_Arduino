#Exercício 01

#Faça um algoritmo que leia um número inteiro e mostre uma mensagem indicando se este número é par ou ímpar e se é positivo ou negativo.

numero = int(input('Digite um número qualquer: '))
resultado = numero % 2 #Retorna o resto da divisão de um número
#print('O resultado foi {}'.format(resultado))
if resultado == 0:
    print('O número {} é PAR'.format(numero))
    if numero >= 0:
        print('POSITIVO'.format(numero))
if resultado == 1:
    print('O número {} é ÍMPAR'.format(numero))
    if numero < 0:
        print('NEGATIVO'.format(numero))