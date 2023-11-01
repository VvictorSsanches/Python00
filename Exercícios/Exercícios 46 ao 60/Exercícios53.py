'''
Crie um programa que leia uma frase qualquer e diga se ela é um palidramo,
desconsidere os espaços
'''
'''
# EU
texto = str(input('Informe uma frase: ')).upper()
texto = ''.join(texto.split(' '))
print('A palavra {} ao contrário é {} e '.format(texto, texto[::-1]))
if texto == texto [::-1]:
    print('É um Palíndromo'.format(texto))
else:
    print('Não é um Palíndromo'.format(texto))
'''
#Guanabara
frase = str(input('Digite uma frase: ')).upper()
palavras = frase.split()
juntos = ''.join(palavras)
inverso = ''
for letra in range(len(juntos)-1, -1, -1):
    inverso += juntos[letra]
print('O inverso de {} é {}'. format(juntos, inverso))
if inverso == juntos:
    print('Temos uma palídromo!')
else:
    print('A frase digitada não é um palídromo')