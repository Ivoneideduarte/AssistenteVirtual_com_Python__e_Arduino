''' Comentário de blocos '''

print('Olá, Mundo!')

print('=' * 50)

nome = 'Ivoneide'
idade = 22
peso = 60
sexo = 'F'

print('O nome é: ' + nome + 'idade: ' + str(idade) + ' peso: ' + str(peso) + ' sexo: ' + sexo)
print('Seu nome é {}, sua idade {}, seu peso {}, seu sexo {} '.format(nome, idade, peso, sexo))

print('=' * 50)

valor = idade + peso
print(valor)

print('=' * 50)

idade1 = '22'
idade2 = '33'
print(idade1 + idade2)

print('=' * 50)

print(type(nome))
print(type(idade))
print(type(peso))
print(type(sexo))

print('=' * 50)

print(3+3)
print(3*3)
print(3**3)
print(3/3)
print(3%3)

print('=' * 50)

x = 10
y = 10

print(x>y)
print(x<y)
print(x==y)
print(x>=y)
print(x<=y)
print(x!=y)

print('=' * 50)

nome = str(input('Digite seu nome: '))
idade = int(input('Informe sua idade: '))
peso = float(input('Informe seu peso:'))
print('O nome do cliente é: {}, ele tem {} anos e pesa {}kg'.format(nome, idade, peso))

print('=' * 50)

ano_nas = int(input('Informe seu ano de nascimento: '))
ano_atual = int(input('Informe o ano atual: '))

idade = ano_atual - ano_nas

if idade < 0:
    print('Infome um ano válido!')
else:
    print('A sua idade é {} anos.'.format(idade))