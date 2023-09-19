#Crie um programa que leia quantos dinheiros uma pessoa tem na carteira e mostre quatos Dólares ele pode comprar | Considere US$1,00 = R$4,86
R = float(input('Infome quanto dinheiro tem na carteira: '))
D = R/4.86
print('Você consegue comprar {:.2f} Dólares.'.format(D))