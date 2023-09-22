#Um professor quer sotear um dos seus alunos para apagar o quadro.
#faça um programa que ajude ele, lendo o nome deles e escrevendo o nome dos alunos 
'''
from random import choice
a1 = str(input('Nome do primeiro aluno: '))
a2 = str(input('Nome do segundo aluno: '))
a3 = str(input('Nome do terceiro aluno: '))
a4 = str(input('Nome do qurto aluno: '))
a5 = str(input('Nome do quinto aluno: '))
a6 = str(input('Nome do sexto aluno: '))
lista = (a1,a2,a3,a4,a5,a6)
alunos = choice(lista)
print('O nome do aluno para apagar o quedro é: {}'.format(alunos.upper()))

ou 

import random

alunos = []
while len(alunos) <5:
    nome_alunos = input ('Nome dos alunos: ')
    alunos.append(nome_alunos)
print('O nome do aluno sorteado foi: {}'.format(random.choice(alunos).upper()))
'''

import random

sorteio = [ 'PEDRA','PAPEL','TESOURA' ]
escolha=str(input('Você quer pedra, papel ou tesoura: ')).upper()
j=sorteio [random.randrange(len(sorteio))]

if escolha== j:
    print(f'Você escolheu {escolha} e seu PC escolheu esse {j}')
    print('Jogue de novo')
#PC ganha
elif escolha=='PEDRA' and j=='PAPEL':
    print (f'Você escolheu {escolha} e seu PC {j}!! Pc ganhou essa')
elif escolha =='PAPEL' and j=='TESOURA':
    print (f'Você escolheu {escolha} e seu PC {j}!! Pc ganhou essa')
elif escolha=='TESOURA' and j=='PEDRA':
    print (f'Você escolheu {escolha} e seu PC {j}!! Pc ganhou essa')
#Vc ganha
elif escolha=='PAPEL' and j=='PEDRA':
    print (f'Você escolheu {escolha} e seu PC {j}!! VC ganhou essa')
elif escolha =='TESOURA' and j=='PAPEL':
    print (f'Você escolheu {escolha} e seu PC {j}!! VC ganhou essa')
elif escolha=='PEDRA' and j=='TESOURA':
    print (f'Você escolheu {escolha} e seu PC {j}!! VC ganhou essa')
#qual quer coisa que não for as três opções cai aqui
else:
    print('Escolha uns das opções')