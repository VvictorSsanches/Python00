'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa, O programa vai perguntar o valor
da casa, o salário do comprador e em quantos anos ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ela não pode exeder 30% do salário ou então o emprestimo será negado
'''

casa = float(input('Valor da casa: R$'))
salário = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
pretenção = casa / (anos * 12)
minimo = salário * 30 / 100
print('Para Pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')
print('a prestação será de  R${:.2f}'.format(pretenção))
if pretenção <= minimo:
    print('Empréstimo pode ser \033[1:32mCONCEDIDO\033[m')
else:
    print('Empréstimo \033[1:31mNEGADO\033[m')