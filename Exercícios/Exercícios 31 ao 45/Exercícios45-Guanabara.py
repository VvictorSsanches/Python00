from random import randint
from time import sleep

itens = ('Papel', 'Pedra', 'Tesoura')
computador = randint(0, 2)

print('''SUA OPÇÕES 
[ 0 ] Papel
[ 1 ] Pedra
[ 2 ] Tesoura''')
jogador = int(input('Qual é a suas jogadas? '))
print('-'*7)
print('  JO')
sleep (0.9)
print('-'*7)
print('  KEN')
sleep (0.6)
print('-'*7)
print('  PO')
sleep(0.3)
print('-=-'*10)
print('    Computador jogou {}'.format(itens[computador]))
print('-=-'*10)
print('     Jogador jogou {}'.format(itens[jogador]))
print('-=-'*10)
if computador == 0: #COMPUTADOR JOGOU PAPEL
    if jogador == 0: #PAPEL
        print('\033[1;33m Empate \033[m')
    elif jogador == 1: #PEDRA
        print('\033[1;31m Computador venceu \033[m')
    elif jogador == 2: #TESOURA
        print('\033[1;32m Jogador Venceu \033[m')    
    else:
        print('Opção invalida')

elif computador == 1: #COMPUTADOR JOGOU PAPEL
    if jogador == 0: #PAPEL
        print('\033[1:32m Jogador Venceu \033[m')
    elif jogador == 1: #PAPEL
        print('\033[1;33m Empate \033[m')
    elif jogador == 2: #TESOURA
        print('\033[1;31m Computador Venceu \033[m')
    else:
        print('Opção invalida')

elif computador == 2: #COMPUTADOR JOGA TESOURA
    if jogador == 0: #PAPEL
        print('\033[1;31m Computador Venceu \033[m')
    elif jogador == 1: #PEDRA
        print('\033[1;32m Jogador Venceu \032[m')
    elif jogador == 2: #TESOURA
        print('\033[1;33mEmpate\033[m')   
    else:
        print('Opção invalida')