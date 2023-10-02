'''
Escreva um programa que pergunte o salário do funcionário e calcule o valor do seu aumento 
Para salário superior a R$1.250,00, calcule o aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.
'''
'''
salário = float(input('Informe o seu salário: '))
if salário > 1250:
    print('O salário irá para {} com 10% de aumento'.format(salário + (salário * 10/100)))
else:
    print('O sálario irá para {} com 15% de aumento'.format(salário + (salário * 15/100)))
'''
valor = float(input('\033[1;31mO valor maximo para alterar: \033[m'))
salário = float(input('\033[1;32mInforme o seu salário: \033[m'))
s15 = salário * 15/100
s10 = salário * 10/100
if salário <= valor:
    novo = salário + (salário * 15/100)
    print('O valor que ganhava R$:\033[1;31m{:.2f}\033[m, com o aumento de 15% R$:\033[0;33m{:.2f}\033[m, totalizando R$:\033[1;32m{:.2f}\033[m.'.format(salário, s15, novo))
else:
    novo = salário + (salário * 10/100)
    print('O valor que ganhava R$:{:.2f}, com o aumento de 10% R$:{:.2f}, totalizando R$:{:.2f}.'. format(salário, s10, novo))
