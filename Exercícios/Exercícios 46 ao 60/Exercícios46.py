'''Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
indo de 10 até 0, com uma passagem de 1 segundo de atraso'''
'''
#insirindo o tempo desejado
from time import sleep
i = int(input('Inicio: '))
f = int(input('Fim'))
for a in range(i, f):
    print(a)
    sleep(1)
print('Estouros')
'''
from time import sleep

for a in range(1,11):
    print(a)
    sleep(0.1)
    
