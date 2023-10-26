'''
Crie um programa que leia uma frase qualquer e diga se ela é um palidramo,
desconsidere os espaços
'''

texto = str(input('Informe uma frase: ')).upper()
texto = ''.join(texto.split(' '))
print('A palavra {} ao contrário é {} e '.format(texto, texto[::-1]))
if texto == texto [::-1]:
    print('É um Palíndromo'.format(texto))
else:
    print('Não é um Palíndromo'.format(texto))