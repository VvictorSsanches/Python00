'''
Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
- O primeiro número é maior 
- O segundo número é maior 
- não existe valor maior, os dois são iguais 

'''

n1 = int(input('Informe o primeiro valor: '))
n2 = int(input('informe o segundo valor: '))

if n1 > n2:
    print('O primeiro valor é {} é maior que o segundo valor {}.'.format(n1,n2))
elif n2 == n1:
    print('O primeiro valor é {} é igual o segundo valor {}.'.format(n1, n2))
else:
    print('O segundo valor é {} é maior que segundo valor {}.'.format(n2, n1))