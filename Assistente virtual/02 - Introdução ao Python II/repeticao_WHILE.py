#O usuário insere números até der na telha

print('Aula 02 - Condicional WHILE')

soma = 0
contador = 0
resp = 's'

#Enquanto a resposta for verdadeira será executado
while resp == 's':
    contador = contador + 1
    n = int(input('Escreva um número: '))
    print('O número digitado foi {}'.format(n))
    soma = soma + n
    print('-=-' * 20)
    resp = input('Deseja escrever outro número? [s/n]: ')
m = soma / contador
print('Programa encerrado, a média dos números é {}'.format(m))
