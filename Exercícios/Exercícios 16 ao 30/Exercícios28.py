'''Escreva um programa que o computador "pensar" em um número Inteiro entre 0 e 5 e peça 
para o usuário tentar descobri qual foi o número escolhido pelo computador
O programa deve escrever se o usuário venceu o perdeu'''
from random import randint
from time import sleep

computador = randint(0, 5) # Faz o computado "PENSAR"

print('\033[1;34;40m-=-\033[m' * 20)
print('\033[1;31;40m Estou pensando em um número entre 0 e 5, Tente adivinhar\033[m')
print('\033[1;34;40m-=-\033[m' * 20)

jogador = int(input('Informe o número a jogar: '))

print('Processndo...')
sleep(1.5)

if jogador == computador:
    print('Voce acertou,\nO número que estava pensando era {} !! \n-=-=-VOCÊ ACERTOU!!-=-=-'.format(computador))
else:
    print('Estava pensando no número {} e não no número {}'.format(computador, jogador))
    print('Voce não conseguiu acertar o número que eu pensei!! \n-=-=-TENTE NOVAMENTE!!-=-=- ')

