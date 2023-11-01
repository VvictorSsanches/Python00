'''
Faça um programa que leia um número inteir e diga se eles é ou não um número primo
'''
'''
num = int(input('Descubra  se um numero é primo '))
isprime = True
current = (num // 2)

for a in range(current, 0, -1):
    if num % a == 0 and a !=1:
        isprime = False

if isprime:
    print('O número {} é primo.'.format(num))
else:
    print('O número {} não é primo'.format(num))
'''
#guanabara
num = int(input('Digite um número: '))
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[34m', end = ' ')
    else:
        print('\033[31m', end = ' ')
    print('{} '.format(c), end = '-')
    