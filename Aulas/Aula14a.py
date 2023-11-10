'''
for c in range (10, -1, -1):
    print(c)
print('Fim')

c = 1
while c < 11:
    print(c)
    c += -1
    break    
print('Fim')
'''
n = 'S'
while n == 'S':
    s = int(input('Digite um número: '))
    n = str(input('Deseja vontinuar? [S/N]: ')).upper()
print('Fim')