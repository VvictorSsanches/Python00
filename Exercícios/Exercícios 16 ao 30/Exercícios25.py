'''
Crie um programa que leia o nome de uma pessoa e diga se ela o nome 'silva' no nome

'''

nome = str(input('Informe o seu nome completo: ')). strip()
print('Seu nome tem silva: {}'.format('Silva' in nome.lower()))