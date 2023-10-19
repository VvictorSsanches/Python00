'''
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade: 

- Se ele ainda vai se alistar ao servoço militar.
- Se é a hora exata de se alistar ou se já passou do tempo do alistamento.
- Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''
from datetime import date
print('Vamos averiguar sua idade para ver quanto tempo falata para se alistar')
idade = int(input('informe o sue ano de nascimento: '))
hoje = date.today().year
if hoje - idade == 18:
    print('O ano de {} é o ano exato que você irá se alistar!'.format(date.today().year))
elif hoje - idade > 18:
    print('O momento do seu alistamento já passou! Ele ocorreu em {}. '.format(idade + 18))
else:
    print('O momento do seu alistamento está por vir! Ele ocorrerá em {}.'.format(idade + 18))
