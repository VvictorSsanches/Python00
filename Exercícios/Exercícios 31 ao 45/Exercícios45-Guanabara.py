from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('''SUA OPÇÕES 
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Qual é a suas jogadas? '))
print('#-=-#'*4)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('#-=-#'*4)
if computador == 0: #COMPUTADOR JOGOU PAPEL
    if jogador == 0: #PAPEL
        print('\033[1;33mEmpate\033[m')
    elif jogador == 1: #PEDRA
        print('Computador venceu')
    elif jogador == 2: #TESOURA
        print('jogador venceu')    
    else:
        print('Opção invalida')

elif computador == 1: #COMPUTADOR JOGOU PAPEL
    if jogador == 0: #PEDRA
        print('Jogador venceu')
    elif jogador == 1: #PAPEL
        print('\033[1;33mEmpate\033[m')
    elif jogador == 2: #TESOURA
        print('Computador Venceu')
    else:
        print('Opção invalida')

elif computador == 2: #COMPUTADOR JOGA TESOURA
    if jogador == 0: #PEDRA
        print('Computador Venceu')
    elif jogador == 1: #PAPEL
        print('Computador Venceu')
    elif jogador == 2: #TESOURA
        print('\033[1;33mEmpate\033[m')   
    else:
        print('')