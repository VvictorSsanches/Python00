'''
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados 
ex: Digiteum número: 1834
Unidade: 4
Dezena: 3
Centena: 8
milhar: 1
'''
'''
num = int(input('Insira númer entre 0 a 9999: '))
#n =str(num)
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número: {}'.format(num))
print('Unidade:{}'.format(u))
print('Dezena: {}'.format(d))
print('Ccentena: {}'.format(c))
print('Milhjar: {}'.format(m))
'''
num = int(input('Infomre o número entre 0 a 9999: '))
print('Analisando número:{}'.format(num))
print('Unidade: {}'.format(num // 1 % 10))
print('Dezena: {}'.format(num // 10 % 10))
print('Centena: {}'.format(num // 100 % 10))
print('Milhar: {}'.format(num // 1000 % 10))