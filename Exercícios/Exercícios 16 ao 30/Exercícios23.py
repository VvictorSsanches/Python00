'''
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados 
ex: Digiteum número: 1834
Unidade: 4
Dezena: 3
Centena: 8
milhar: 1
'''

num = int(input('Insira o valor enre 0 a 9999: '))
a = num[4]
print('Unidade:{}'.format(a))
