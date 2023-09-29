'''
Crie um programa que leia um número inteiro e mostre na sua tela se ele é par ou impar
'''

valor = int(input('Informe um valor iteiro: '))
if valor % 2 == 0:
    print('Esse número é par'.format(valor))
else:
    print('Esse número é impar'.format(valor))