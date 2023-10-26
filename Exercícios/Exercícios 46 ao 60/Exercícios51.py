'''
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. (Progressão Aritmética).
No final, mostre os 10 primeiros termos dessa progressão 
'''

term1 = int(input('Informe o primeiro termo: '))
dif = int(input('Informe a razão do PA: '))
termg = term1 +(10 - 1)*dif
for c in range (term1, termg, dif):
    print('{}'.format(c))
print('FIM')