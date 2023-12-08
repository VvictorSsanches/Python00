'''Calcule o reajuste salarial por faixas( até R$ 1500 reajuste de 20%, de R$ 1500 a R$ 2500 reajuste de 15%, de 2500 a R$ 3200 reajuste de 12%
e a cima de R$3200 reajuste de 8%)
'''
'''salário = float(input('\033[1;32mInforme o seu salário: \033[m'))
s20 = salário * 20/100
s15 = salário * 15/100
s12 = salário * 12/100
s8 = salário * 8/100

if salário < 1500:
    novo = salário + (salário * 20/100)
    print('O valor que ganhava R$:\033[1;31m{:.2f}\033[m, com o aumento de 15% R$:\033[0;33m{:.2f}\033[m, totalizando R$:\033[1;32m{:.2f}\033[m.'.format(salário, s15, novo))
else:
salário <= 1500 <= 2500
    novo = salário + (salário * 10/100)
    print('O valor que ganhava R$:{:.2f}, com o aumento de 10% R$:{:.2f}, totalizando R$:{:.2f}.'. format(salário, s10, novo))
'''

sal = int(input('Informe o seu salário: '))
n1 = sal * 0.20
n2 = sal * 0.15
n3 = sal * 0.12
n4 = sal * 0.08

novo = sal + (sal * 20/100)
if sal <= 1500:
    print('O valor que ganhava R$:\033[1;31m{:.2f}\033[m, com o aumento de 20% R$:\033[0;33m{:.2f}\033[m, totalizando R$:\033[1;32m{:.2f}\033[m.'.format(sal, n1, novo))

elif  sal > 1500 or sal <= 2500:
    novo = sal + (sal * 15/100)
    print('O valor que ganhava R$:\033[1;31m{:.2f}\033[m, com o aumento de 15% R$:\033[0;33m{:.2f}\033[m, totalizando R$:\033[1;32m{:.2f}\033[m.'.format(sal, n2, novo))

elif sal > 2500 or sal < 3200:
        novo = sal + (sal * 12/100)
        print('O valor que ganhava R$:\033[1;31m{:.2f}\033[m, com o aumento de 12% R$:\033[0;33m{:.2f}\033[m, totalizando R$:\033[1;32m{:.2f}\033[m.'.format(sal, n3, novo))

else:
    sal > 3200
    novo = sal + (sal * 8/100)
    print('O valor que ganhava R$:\033[1;31m{:.2f}\033[m, com o aumento de 8% R$:\033[0;33m{:.2f}\033[m, totalizando R$:\033[1;32m{:.2f}\033[m.'.format(sal, n4, novo))    