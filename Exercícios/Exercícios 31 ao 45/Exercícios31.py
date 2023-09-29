'''
Desenvolva um programa que pergunte a distância em uma viajem em Km.
Calcule o preço da passagem, cobrada R$0,50 por km para viajar até 200km em R$0,45 para
viajens mais longas
'''

km = int(input('Informe a distancia da viajem: '))
if km <= 200:
    print('valor a pagar até 200Km será de {:.2f}'.format(km * 0.50))
else:
    print('Valor a pagar a cima de 200Km será de {:.2f}'. format(km * 0.45))