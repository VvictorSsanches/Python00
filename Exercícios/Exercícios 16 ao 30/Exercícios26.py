'''
Faça um programa que leia uma frase pelo teclado e mostre:
> Quantas vezes aparece a letra 'A'.
> Em que posição ela aparece a primeira vez
> em que posição ela aparece a última vez.
'''

frase = (str(input('Informe uma frase: '))).strip().upper()
print('Quantas vezes aparece a letra (A):{}'.format(frase.count('A')))
print('Em qual posição a letra (A) aparece na primeira vez?{}'.format(frase.find('A') + 1))
print('Em qual posição apararece a ultima letra (A)? {}'.format(frase.rfind('A') + 1))
