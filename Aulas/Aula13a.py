'''
for c in range(0, 6):
    print('oi')
print('FIM')
print('-=-'*5)

for c in range(0, 6):
    print(c)
print('FIM')
print('-=-'*5)

for c in range (0,4):
    print('passo')
    print('Pulas')
print('passo')
print('pegar')
print('-=-'*5)

for c in range(0, 10, 3):
    print(c)
print('fim')

i = int(input('Inicio: '))
f = int(input('fim: '))
p = int(input('passo: '))
for c in range(i, f+1, p):
    print(c)
print('fim')
'''
for c in range(0, 3):
    n = int(input('Digite um valor'))
print('FIM')

s = 0
for c in range (0, 4):
    n = int(input('Informe um número: '))
    s += n
print('A somatoria entre os valores é {}'.format(s))