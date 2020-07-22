#Exercício 03

#Escreva um algoritmo que receba o código correspondente ao cargo de um funcionário de uma escola e seu salário atual. Mostre o valor do novo salário, com aumento, conforme tabela abaixo:

print('-=-' * 10)
print('[1] Secretário  +45%')
print('[2] Tesoureiro  +35%')
print('[3] Professor   +25%')
print('[4] Coordenador +15%')
print('[5] Diretor')
print('-=-' * 10)

codigo = int(input('Informe o seu código: '))

if codigo == 1:

    print('Seu cargo é de Secretário')
    salario = float(input('Qual o seu sálario atual? R$'))
    novo = salario + (salario * 45 / 100)
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario, novo))

elif codigo == 2:

    print('Seu cargo é de Tesoureiro')
    salario = float(input('Qual o seu sálario atual? R$'))
    novo = salario + (salario * 35 / 100)
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario, novo))

elif codigo == 3:

    print('Seu cargo é de Professor')
    salario = float(input('Qual o seu sálario atual? R$'))
    novo = salario + (salario * 25 / 100)
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario, novo))

elif codigo == 4:

    print('Seu cargo é de Coordenador')
    salario = float(input('Qual o seu sálario atual? R$'))
    novo = salario + (salario * 15 / 100)
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario, novo))

elif codigo == 5:

    print('Seu cargo é de Diretor')
    print('Não tem aumento')
else:
    print('Código inválido!')