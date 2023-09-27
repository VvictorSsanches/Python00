'''
Crie um programa que leia o nome completo de uma pessoa e mostre.
> O nome com todas as letras maiúsculas.
> O nome com todas minúsculas.
> Quantas letras ao tedo (sem considerar espaços).
> Quantas letras tem o primeiro nome 

'''

nome = str(input('Insira o seu nome: ')).strip()
print('Seu nome em minúsculo é: {}'.format(nome.lower()))
print('Seu nome em maiúsculo é: {}'.format(nome.upper()))
print('Seu nome tem ao todo: {} letras'.format(len(nome)- nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))

