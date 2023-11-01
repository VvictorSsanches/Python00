'''
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for impar, desconsidere-o
'''
'''
s = 0
a = int(input('informe o valor: '))
for num in range (1, a + 1):
    if num % 2== 0:
        s += num
print(s)     
'''    
'''
soma = 0
cont = 0
for c in range(1,7):
    num = int(input('Digite o {} valor: '.format(c)))
    if num % 2 == 0:    
        soma += num
        cont += 1
print('Você informou {} números Pares e a soma foi {} '.format(cont, soma))
'''
for c in range(0,50):
    if c % 2  == 0:
        print(c + 1, end=" ")