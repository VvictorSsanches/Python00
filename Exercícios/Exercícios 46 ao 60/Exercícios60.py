'''
Faça um programa que leia um número qualquer e mostr o seu fatorial.

Ex = 5x4x3x2x1 = 120
'''

'''
from math import factorial
n = int(input('Digite um número para calcular o seu fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}'.format(n,f))
'''

n = int(input('Informe o número para calcular o fatorial: '))
c = n
f= 1
print('Calculando {} ! = '.format(n), end= ' ')
while c > 0:
    print('{}'.format(c),end=' ')
    print(' x 'if c > 1 else ' = ',end=' ')
    f *= c
    c -= 1
print ('{}'.format(f))
