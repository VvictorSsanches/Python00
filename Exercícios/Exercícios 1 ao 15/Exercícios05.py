#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.
x = int(input('informe um número'))
n = x - 1
m = x + 1
print('O valor inteiro informado foi {}, o seu sucessor é {}, e o antecessor é {}.'.format(x, n, m))

# ou

x = int(input('informe um número'))
print('O valor inteiro informado foi {}, o seu sucessor é {}, e o antecessor é {}.'.format(x, (x-1), (x+1) ))