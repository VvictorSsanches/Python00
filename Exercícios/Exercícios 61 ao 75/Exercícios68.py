'''
Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando o jogardor PERDER,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
'''

from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('Par ou Impar? [P/I]').strip().upper()[0])
    print(f'Você jogou {jogador} e o computador jogou {computador}. total de {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!!')
            v += 1
        else:
            print('Você perdeu!!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu!!')
            v += 1
        else:
            print('Você Perdeu!!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes.')