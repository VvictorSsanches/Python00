'''
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.'''

n1 = float(input('infomre o primeiro número: '))
n2 = float(input('informe o segundo número: '))
n3 = float(input('informe o terceiro número: '))
# Verificar quem é o menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

# Verificar que é o maior 
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print('O menor núemro é {} e o maior número E {}'.format(menor, maior))