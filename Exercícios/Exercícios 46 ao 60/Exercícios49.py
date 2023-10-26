'''
Refaça o desafio 09, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando o 
laço for.
'''

num = int(input('Informe um valor para ver a Tabuada: '))

for tab in range(1,11):
    print('{} x {} = {}'.format(num, tab ,num *tab))