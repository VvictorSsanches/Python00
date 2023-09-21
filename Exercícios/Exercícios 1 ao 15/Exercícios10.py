#Crie um programa que leia quantos dinheiros uma pessoa tem na carteira e mostre quatos Dólares ele pode comprar | Considere US$1,00 = R$4,86
R = float(input('Infome quanto dinheiro tem na carteira? R$'))
D = R/4.86
Y = R/0.0037
E = R/5.1989
print('Com R${:.2f} você consegue comprar US${:.2f} '.format(R, D))
print('Com R${:.2f} você consegue comprar ¥{:.2f}'.format(R, Y))
print('Com R${:.2f} você consegue comprar €{:.2f}'.format(R, E))