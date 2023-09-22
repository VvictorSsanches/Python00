#Crie umn programa que leia um número Real qualquer pelao teclado e mostre na tela a sua portção inteira.
# Ex: Digite um número: 6.127 o número 6.127 tem a parte inteira 6. 

import math
n = float(input('informe algum valor qubrado para mostar o inteiro: '))
print('O porção inteira de {} é {}'.format(n, math.trunc(n)))

ou

from math import trunc
num = float(input('digite um valor'))
print('O valor digitado foi {} e a sua portção inteira é {}'.format(num, trunc(num)))

ou

n = float(input('Digite um valor'))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(n, int(n)))