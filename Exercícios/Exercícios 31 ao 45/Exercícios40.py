'''
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no
final, de acordo com a média atingida: - Média abaixo de 5.0: REPROVADO - Média entre 5.0 e 6.9:
RECUPERAÇÃO - Média 7.0 ou superior: APROVADO
'''

n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota:'))
n = (n1 + n2) / 2
print('A media entre {:.2f} e {:.2f} é {:.2f}.'.format(n1, n2, n))
if n >= 7.0:
    print('Aprovado')
elif n >= 5.0:
    print('Recuperção')
else:
    print('Reprovado')