'''
Crie um programa que leia o ano de nascimento de sete pessoas. no final, mostre quantas pessoas 
ainda não atingiram a maioridade e quantas já são de maiores.
'''
'''
from datetime import date

print('Vamos averiguar se é maior de idade')

hoje = date.today().year

ano = 0
maior = 0
menor = 0

for a in range(0,8):
    ano = int(input('Digite o ano de nascimento: '))
    idade = hoje - ano
    if idade > 18:
        maior = maior + 1
    else:
        menor = menor + 1
print('Maiores de idade {}'.format(maior))
print('Menores de idade {}'.format(menor))
'''
#Guanabara

from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range (1, 8):
    nas = int(input('Em que ano a {}° pessoa nasceu? '.format(pess)))
    idade = atual - nas
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maior de idade!'.format(totmaior))
print('Ao todo tivemos {} pessoas menor de idade!'.format(totmenor))