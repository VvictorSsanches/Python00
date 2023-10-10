'''
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento
de um atleta e mostre sua categoria, de acordo com a idade: - Até 9 anos: MIRIM - Até
14 anos: INFANTIL - Até 19 anos: JÚNIOR - Até 25 anos: SÊNIOR - Acima de 25 anos: MASTER
'''

from datetime import date

print('Bem vindo a Confederação Nacional de Natação')
idade = int(input('Informe o seu ano de nascimento: '))
hoje = date.today().year
print('Sua idade é {}.'.format(hoje))
if hoje - idade <= 9:
    print('bem vindo ao grupo Mirim')
elif hoje - idade <= 14:
    print('Bem vindo ao grupo Infantil')
elif hoje - idade <= 19:
    print('Bem vindo ao grupo Júnior')
elif hoje - idade <= 25:
    print('Bem vindo ao Grupo Sênior')
else:
    print('Bem vindo ao Grupo Master')

