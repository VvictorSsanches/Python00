'''
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for impar, desconsidere-o
'''

s = 0
a = int(input('informe o valor: '))
for num in range (a):
    if num % 2== 0:
        s += num
print(s)     
    

