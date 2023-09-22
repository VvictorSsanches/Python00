#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, 
#calcule e mostre o comprimento da hipotenusa
'''
cateto_o = float(input('Informe o compimento do cateto oposto'))
cateto_a = float(input('Informe o comprimento do cateto adjacente')) 
hi = (cateto_a ** 2 + cateto_o ** 2 ) ** ( 1 / 2 )
print('A hipotenusa vai medir {:.2f}'.format(hi))

ou
'''
import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)
print('A hipotenusa vai medir{:.2f}'.format(hi))
