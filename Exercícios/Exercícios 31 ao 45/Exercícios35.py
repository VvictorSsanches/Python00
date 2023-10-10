'''
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
R1 -----
R2 ----------
R3 -------
'''
print('-=-' * 20)
print('Analisador de Triãngulos')
print('-=-' * 20)

a1 = float(input('Insira o primeiro comprimento: '))
a2 = float(input('Insira o segundo comprimento: '))
a3 = float(input('Insira o terceiro comprimento: '))

if a1 + a2 > a3 and a2 + a3 > a1 and a3 + a1 > a2:
    print('Prodemos formar um riangulo.')
else:
    print ('Não podemos Formar um triangulo.')
    

if l2 + l3 > l1 and l2 + l1 > l3 and l1 + l2 > l3:
    print('O triângulo \033[1;34mexiste\033[m', end='')
    if l1 == l2 and l1 == l3:
        print(' e é equilátero.')
    elif l1 != l2 and l1 != l3:
        print(' e é escaleno.')
    l2 == l3 and l2 != l1:
        print(' e é isósceles.') # Essa parte do isósceles dá pra por apenas um "else:"
else:
    print('O triângulo \033[1;31mnão\033[m existe.')
