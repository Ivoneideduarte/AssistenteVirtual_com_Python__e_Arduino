'''
#Declaração de variáveis
x = 0
y = 0
z = 0

def calculadora(y, z): #Função
    n = y + z
    print('A soma temporária é: {}'.format(n))

while (x<5):
    x = x + 1
    y = y + 1
    z = z + 2
    calculadora(y, z)
'''

'''
#Declaração de variáveis
n = 0

def calculadora(z): #Função
    global n
    n = n + z
    print('A soma temporária é: {}'.format(n))

while True:
    z = int(input('Digite outro número: '))
    calculadora(z)
'''
#Declaração de variáveis
m = 0

def calculadora(x=0, y=0, z=0): #Função
    global m
    m = x + y + z
    print(f'A soma temporária é: {m}')

#Programa principal
while True:
    print('Programa principal')

    x = int(input('Digite um número: '))
    y = int(input('Digite outro número: '))
    z = int(input('Digite outro número: '))
    calculadora(x)
    calculadora(x, z)
    calculadora(x, y, z)
    calculadora(y, z)

    if m > 30:
        print('Sua conta estorou.')
        break

print('Não entrei em canto nenhum.')
