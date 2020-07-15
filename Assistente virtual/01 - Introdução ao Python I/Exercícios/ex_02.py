#Exercício 02

#Faça um algoritmo que leia a primeira letra do estado civil de uma pessoa e mostre uma mensagem com a sua descrição (Solteiro, Casado, Viúvo,Divorciado). Mostre uma mensagem de erro, se necessário.

print('=' * 25)
print('Digite S para Solteiro')
print('Digite C para Casado')
print('Digite V para Viúvo')
print('Digite D para Divorciado')
print('=' * 25)

estado_civil = str(input('Informe o seu estado cívil: ')).upper()
if estado_civil == 'S':
    print('Solteiro')
if estado_civil == 'C':
    print('Casado')
if estado_civil == 'V':
    print('Viúvo')
if estado_civil == 'D':
    print('Divorciado')
