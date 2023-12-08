'''
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. 
No final, mostre:
A) Qual é o total gasto na compra.
B) Quantos produtos custam maius de R$1000.
C) Qual o nome do produto mais barato.
'''
valorg = acima1000 = prodb = 0
while True:
    produto = int(input('Nome do produto: '))
    acmde1000 = ' '
    while acmde1000 not in 1000:
        acmde1000 = int(input('Informe o valor do produto: '))
    if acmde1000 > 1000:
        valorg += 1 
    if acmde1000 < 250:
        valorg +=1
    if produto < 100:
        valorg += 0
    resp = ''    
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
