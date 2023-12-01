'''
Melhore o desafio 61, perguntando para o usuário se le equer mostrar mais alguns termos. 
O programa encerra quando ele disser que quer mostrar 0 termos.
'''

print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1 
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} > '.format(termo),end=' ')
        termo = termo + razão
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar mais? '))
print('Progressão finalizaod com o {} termos mostrados.'.format(total))
    