print('AULA 02 - Condicional SWITCH/CASE gambiarra')

x = int(input('Digite um número: '))

'''if x == 0: #if x is 0:
    print('Você está na porta zero.')
elif x == 1:  #if x is 1:
    print('Você está na porta um.')
elif x == 2:  #if x is 2:
    print('Você está na porta dois.')
else:
    print('Você está na porta avulsa.')'''

if x == 0:
    print('Você está na porta zero.')
elif x in (1, 3):
    print('Você está na porta um ou na três.')
elif x == 2:
    print('Você está na porta dois.')
else:
    print('Você está na porta avulsa.')