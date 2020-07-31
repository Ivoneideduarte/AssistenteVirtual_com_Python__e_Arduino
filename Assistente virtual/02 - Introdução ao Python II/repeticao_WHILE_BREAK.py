'''
#Exemplos
Enquanto Verdadeiro
    se chão
        passo
    se buraco
        pula
    se moeda
        pega
    se trofeu
        pula
        interrompa
pega

while True:
    if chão:
        passo
    if buraco:
        pula
    if moeda
        pega
    if trofeu:
        pula
        break #Encerra o programa, sai para fora do programa de repetição
pega
'''

'''
cont = 1
while cont <= 10:
    print(cont, '-> ', end='')
    cont += 1
print('Acabou')
'''
'''
n = 0
while n != 999:
    n = int(input('Digite um número: '))
'''

'''
n = cont = 0
while cont < 3:
    n = int(input('Digite um número: '))
    cont += 1
'''

'''n = s = 0
while n != 999:
    n = int(input('Digite um número: '))
    s += n

print('A soma vale {}'.format(s))'''

'''n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n

#print('A soma vale {}'.format(s))
print(f'A soma vale {s}') #f string'''

nome = 'José'
idade = 33
salario = 987.3
print(f'O {nome} tem {idade} anos e ganha R${salario:.2f}.')