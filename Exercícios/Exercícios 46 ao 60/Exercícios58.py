'''
Melhoe o jogo do desafio 28 aonde o computador vai 'pensar' em um número de 0 a 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palites foram necessários para vencer

'''
from random import randint
computador = randint (0, 10)
print('Sou seu computador... Acabei de pensar em um npumero entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0 
while not acertou:
    jogador = int(input('Qual o seu Palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais.. Tente mais uma vez.')
        else:
            print('Menos.. Tente mais uma vez')
print('Acertou com {} palpites. Parabens'.format(palpites))