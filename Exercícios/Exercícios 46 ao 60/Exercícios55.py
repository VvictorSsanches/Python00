'''
Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos.
'''

maior = 0 
menor = 0

for c in range(1,6):
    peso = float(input('Informe o peso da {}° pessoa: '.format(c)))

    if c ==1:
        maior = peso
        menor = peso

    else:
        if peso > maior:
            meior = peso
        if peso < menor:
            menor = peso

print('Maior peso {}Kg.'.format(maior))
print('Menor peso {}Kg.'.format(menor))