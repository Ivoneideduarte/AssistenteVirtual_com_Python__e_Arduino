#Recebe 3 notas, calcula a média e se for maior que 7 retorna aprovado se for menor que 7 retorna reprovado

print('Aula 02 - Condicional IF')

n1 = float(input('Insira a nota 01: '))
n2 = float(input('Insira a nota 02: '))
n3 = float(input('Insira a nota 03: '))

m = (n1 + n2 + n3)/3
#print('A média do aluno é {:.1f}'.format(m))

if m >= 7:
    print('O aluno passou com a média {:.1f}'.format(m))

elif 7 > m >= 4:
    print('O aluno está de recuperação com a média {:.1f}'.format(m))
    nr = float(input('Insira a nota de recuperação: '))
    r = (nr + m)/2 #Nota de recuperação
    if r >= 7:
        print('O aluno de passou com a média {:.1f}'.format(r))
    else:
        print('O aluno reprovou com a média de recuperação {:.1f}'.format(r))
else:
    print('O aluno reprovou com a média {:.1f}'.format(m))

