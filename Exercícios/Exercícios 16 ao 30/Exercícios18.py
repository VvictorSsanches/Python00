#Faça um programa que leia um Ãngulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse 
'''
import math
an = float(input('Digite um ãngulo que você deseja: '))
se = math.sin(math.radians(an))
print('O ângulo de {} tem o SENO de {:.2f}'.format(an, se))
co = math.cos(math.radians(an))
print('O ângulo de {} tem COSENO de {:.2f}'.format(an, co))
ta = math.tan(math.radians(an))
print('O ângulo de {} tem TANGENTE de {:.2f}'.format(an, ta))
'''

from math import sin, cos, tan, radians
an = float(input('Digite um ângulo que deseja: '))
print('O ângulo de {} tem o SENO de {:2f}'.format(an, sin(radians(an))))
print('O ângulo de {} tem o COSENO de {:.2f}'.format(an, cos(radians(an))))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(an, tan(radians(an))))
