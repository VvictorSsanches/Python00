'''
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. (Progressão Aritmética).
No final, mostre os 10 primeiros termos dessa progressão 
'''
'''
#Que eu fiz
term1 = int(input('Informe o primeiro termo: '))
dif = int(input('Informe a razão do PA: '))
termg = term1 +(10 - 1)*dif
for c in range (term1, termg, dif):
    print('{}'.format(c))
print('FIM')
'''
#Guanabara
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
decimo = primeiro + (10 - 1)*razão
for c in range (primeiro, decimo + razão, razão):
    print('{} '.format(c), end="-> ")
print('FIM')