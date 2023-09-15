#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo a todas as informações possiveis

x = input('Digite algo: ')
print(type(x))
print('É um número?: ', x.isnumeric())
print('É um espaço?: ', x.isspace())
print('É alfabético?: ', x.isalpha())
print('É alfanúmerico?:', x.isalnum())
print('Esta em Maiusculo?: ', x.isupper())
print('Esta em Minusculo?: ', x.islower())
print('Esta Captalizada?: ', x.istitle())
