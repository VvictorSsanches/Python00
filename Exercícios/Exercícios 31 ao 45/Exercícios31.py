'''
Desenvolva um programa que pergunte a distância em uma viajem em Km.
Calcule o preço da passagem, cobrada R$0,50 por km para viajar até 200km em R$0,45 para
viajens mais longas
'''
'''
km = int(input('Informe a distancia da viajem: '))
if km <= 200:
    print('valor a pagar até 200Km será de {:.2f}'.format(km * 0.50))
else:
    print('Valor a pagar a cima de 200Km será de {:.2f}'. format(km * 0.45))
'''
'''
distancia = int(input('Informe o caminho que irá percorrer: '))
disa = distancia * 0.50
disb = distancia * 0.45

if distancia <= 200:
    print('o valor a pagar se andar mens de 200Km será de {:.2f}'.format(disa))
else:
    print('O valor a pagar se for a mais de 200Km será de {:.2f}'.format(disb))
'''
distância = float(input('Qual é a distância da sua viajem? '))
print('Você esta preste a começar uma viajem de {}Km'.format(distância))
preço = distância * 0.50 if distância <= 200 else distância * 0.45
print('E o preço da sua passagem sera de R${:.2f}'.format(preço))