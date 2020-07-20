print('AULA 02 - Condicional FOR')

"""O usuário insere números até der na telha"""

"""Incremente um número x vezes"""

for x in range(0, 6, 2): #Inicialização, Condição e Incremento
    print(x) #Impressão

print('Parametro do incremento default')
for x in range(0, 6): #Subtende-se o incremento
    print(x) #Impressão

print('Parametro do incremento e inicialização default')
for x in range(5): #Subtende-se o incremento a Inicialização e o Incremento
    print(x) #Impressão

print('Decremento')
for x in range(10, 0, -2):
    print(x) #Impressão

print('Último FOR')
for x in [1, 2, 3, 4, 5, 6, 7]:
    print(x)

for x in ("Ivoneide", "Yandra", "Mariana", "Eliezer"):
    print(x)