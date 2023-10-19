'''
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no
final, de acordo com a média atingida: - Média abaixo de 5.0: REPROVADO - Média entre 5.0 e 6.9:
RECUPERAÇÃO - Média 7.0 ou superior: APROVADO
'''

n1 = int(input('Informe a primeira nota: '))
n2 = int(input('informe a segunda nota: '))
nota = (n1 + n2) / 2 
print('Tirando {:.1f} e {:.1f}, a media é de {:.1f}'.format(n1, n2, nota))
if 7 > nota >= 5:
    print('O aluno está de RECUPERAÇÃO.')
elif nota < 5:
    print('O aluno foi REPROVADO')
elif nota >= 7:
    print('O aluno foi APROVADO')