'''
Faça um programa que leia  o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

ex: Ana Maria de Souza
Primeiro: Ana 
Ultimo: Souza
'''
nome = str(input('Escreva o seu nome completo: ')).strip()
n = nome.split()
print('Seu primeiro nome é: {}'.format(n[0]))
print('Seu ultimo nome é: {}'.format(n[len(n)-1]))