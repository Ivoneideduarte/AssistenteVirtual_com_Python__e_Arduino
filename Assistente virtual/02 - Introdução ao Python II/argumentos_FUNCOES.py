'''
#Rotinas
def mostraLinha():
    print('-' * 25)


#Programa principal
mostraLinha() #Faz a chamada da função
print(' SISTEMA DE ALUNOS ')
mostraLinha()

mostraLinha()
print(' CADASTRO DE FUNCIONÁRIOS ')
mostraLinha()

mostraLinha()
print(' ERRO NO SISTEMA ')
mostraLinha()
'''

'''
#Funções com parâmetros
def mensagem(msg):
    print('-' * 25)
    print(msg)
    print('-' * 25)

#Programa principal
mensagem('SISTEMA DE ALUNOS')
mensagem('CADASTRO DE FUNCIONÁRIOS')
mensagem('ERRO NO SISTEMA')
'''


def soma(a, b):
    s = a + b
    print(f'Soma vale: {s}')


#Programa principal
'''
a = 4
b = 5
s = a + b
print(s)

a = 8
b = 9
s = a + b
print(s)

a = 2
b = 1
s = a + b
print(s)
'''

soma(a = 4, b = 5)
soma(8, 9)
soma(2, 1)


'''
def contador(* num): #Desempacota
    for valor in num:
        print(f'{valor} ', end='')
    print('FIM!')


#Empacotamento
contador(5, 7, 3, 1, 4)
contador(8, 4, 7)
'''
'''
def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


#Listas
valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)
'''

'''def soma(* valores): #Desempacotamento
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}.')


soma(5, 2)
soma(2, 9, 4)'''