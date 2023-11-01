'''
Faça um programa que mostrte na tela todos os núeros pares que estão no intervalo de 1 até 50

'''
#Números Pares
for a in range(1,51):
    if a %2 == 0:
        print(a, end=' ')
print('-'*1)
# números Impares
for c in range(0,50):
    if c % 2  == 0:
        print(c + 1, end=" ")