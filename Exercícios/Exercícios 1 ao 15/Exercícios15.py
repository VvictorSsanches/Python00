# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelas quais foram alugado. 
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dia = int(input('Infome quantos dias usou o carro? '))
km = float(input('Infomre quantos Km foram rodados? '))
D = dia*60
K = km*0.15
DK = D+K
print('O total a pagar R${}!'.format(DK))
 
# OU

dia = int(input('Dias com o carro? '))
km = float(input('Km rodados? '))
DK = ( dia * 60 ) + ( km * 0.15 ) 
print('O toatal a pagar é R${:.2f}!'.format(DK))