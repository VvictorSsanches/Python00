'''
Escreva um programa que leia um número inteiro qualuqer e peça para o usuário escolher qual será a base de conversão

- 1 para Binário
- 2 para Octal
- 3 para hexadecimal
'''

num = int(input('Informe o Valor:'))
escolha = int(input('Escolha o tipo de conversão: \n[1] Binário \n[2] Octal \n[3] Hexadecimal \nDigite aqui:'))

if escolha == 1:
    print('A conversão de {} para binário é {}'.format(num, bin(num)[2:]))
elif escolha == 2:
    print('A conversão de {} para Octal é {}'.format(num, oct(num)[2:]))
elif escolha == 3:
    print('A conversão de {} para Hexadecimal é {}'.format(num, hex(num)[2:]))
    
