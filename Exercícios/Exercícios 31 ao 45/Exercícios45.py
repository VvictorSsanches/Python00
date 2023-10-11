'''
Crie um programa que faça o computador jogar Jokenpô com você.
'''

from random import randint
from time import sleep
print('-=-'*6)
print(' Escolha a baixo')
print('-=-'*6)
escolha = (1, 2, 3)
j = randint(1,3)

sort = int(input('[1] Papel \n[2] Pedra \n[3] Tesoura \nQual vai ser? '))

print('Jo')
sleep(1.2)
print('Ken')
sleep(0.6)
print('Po')
sleep(0.3)
# escolha do jogador
'''if escolha == j:
    print('Você escolheu {} e seu pc escolheu {}'.format(escolha,j))
''' 
#PC ganha
if escolha == 1 and j == 2:
    print('Você escolheu {} e o seu PC escolheu {} \nPC Ganhou nessa!!'.format(escolha[j],j))
elif escolha == 2 and j == 3:
    print('Você escolheu {} e o seu PC escolheu {} \nPC Ganhou nessa!!'.format(escolha[j],j))
elif escolha == 3 and j == 1:
    print('Você escolheu {} e o seu PC escolheu {} \nPC Ganhou nessa!!'.format(escolha[j],j))
'''
#Você Ganha
if escolha == 2 and j ==1:
    print('Você escolheu {} e o seu PC escolheu {} \nVocê Ganhou !!'.format(escolha, j))
elif escolha == 3 and j == 2:
    print('Você escolheu {} e o seu pc escolheu {} \nVocê Ganhou !!'.format(escolha, j))
elif escolha == 1 and j == 3:
    print('Você escolheu {} e o seu pc escolheu {} \nVocê ganhou !!'.format(escolha, j))
'''