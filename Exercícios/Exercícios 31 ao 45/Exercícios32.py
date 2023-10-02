'''
Faça um programa que leia um ano qual qualuqer e mostre se ele é bissexto'''

from datetime import date
ano = int(input('Informe o ano para saber se é bissexto, se quiser saber o ano atual informe 0: '))
#Ano Atual
if ano == 0:
    ano = date.today().year
#Ano Atual    
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))
