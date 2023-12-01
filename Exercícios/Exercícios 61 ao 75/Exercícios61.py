'''
Refaça o desafio 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progerssão usando a estrurua while

'''

print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1 
while cont <= 10:
    print('{} > '.format(termo),end=' ')
    termo = termo + razão
    cont += 1
print('FIM')