'''
Faça um programa que leia o sexo de uma pessoa, mas só aceitar os valores
'M' ou 'F'.
Caso esteja erraqdo, peça a digitação novamnete até ter um valor correto
'''
s = str(input('Informe seu sexo: [F/M] ')).strip().upper()[0]
while s not in 'FfmM':
    s = str(input('Dados Invalidos, Por Favor, imsira seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(s))