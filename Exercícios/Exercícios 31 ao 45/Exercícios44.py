'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal
e condição de pagamento: - à vista dinheiro/cheque: 10% de desconto - à vista no cartão: 5% de
desconto - em até 2x no cartão: preço formal - 3x ou mais no cartão: 20% de juros
'''
'''
QUAL METODO DE PAGAMENTO 
DINHIRO/CHQUE = 10% DESCONTO 
CARTÃO A VISTA 5% DESCONTO 
EM ATÉ 2X PREÇO NORMLA 
MAIS Q 3X 20% JUROS
'''
valor = float(input('Valor do produto: '))
pag = [1, 2, 3, 4]
print('[1] Dinheiro, [2]')