'''
Crie um programa que faça o computador jogar Jokenpô com você.
'''
from random import randrange
from time import sleep

print('-=-'*6)
print(' Escolha a baixo')
print('-=-'*6)

escolha = ['Papel', 'Pedra', 'Tesoura']
j = escolha [randrange(len('Papel', 'Pedra', 'Tesoura'))]


sort = str(input('[0] Papel \n[1] Pedra \n[2] Tesoura \nQual vai ser? '))
'''
print('Jo')
sleep(1.2)
print('Ken')
sleep(0.6)
print('Po')
sleep(0.3)
'''
# escolha do jogador
if escolha == j:
    print('Você escolheu {} e seu pc escolheu {}'.format(escolha,j))
#PC ganha
elif escolha == 0 and j == 1:
    print('Você escolheu {} e o seu PC escolheu {} \nPC Ganhou nessa!!'.format(escolha[j],j))
elif escolha == 1 and j == 2:
    print('Você escolheu {} e o seu PC escolheu {} \nPC Ganhou nessa!!'.format(escolha[j],j))
elif escolha == 2 and j == 0:
    print('Você escolheu {} e o seu PC escolheu {} \nPC Ganhou nessa!!'.format(escolha[j],j))
#Você Ganha
elif escolha == 1 and j ==0:
    print('Você escolheu {} e o seu PC escolheu {} \nVocê Ganhou !!'.format(escolha, j))
elif escolha == 2 and j == 1:
    print('Você escolheu {} e o seu pc escolheu {} \nVocê Ganhou !!'.format(escolha, j))
elif escolha == 0 and j == 2:
    print('Você escolheu {} e o seu pc escolheu {} \nVocê ganhou !!'.format(escolha, j))
else:
    print('Tente novamente!!')

