'''
Crie um programa que leia dois valores e mostre um menu no tela:

[1] somar
[2] multiplicar
[3] maior 
[4] novos números
[5] sair do programa

seu programa deverá realizar a operação solicitada em cada caso.
'''

n1 = int(input('Informe o primeiro valor: '))
n2 = int(input('Informe o segundo valor: '))

opção = 0
while opção != 5:

    print('''[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números 
[ 5 ] Sair do programa''')
    opção = int(input('>>>>> Qual a sua opção '))
    
    if opção == 1:
        soma = n1 + n2
        print('A soma entre os valores {} + {} é {}.'.format(n1,n2,soma))
    
    elif opção == 2:
        mult = n1 * n2
        print('A multiplicação entre {} * {} é {}.'.format(n1,n2,mult))
    
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior é {}'.format(n1,n2,maior))
    
    elif opção == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Infomre o primeiro valor: '))
        n2 = int(input('Informe o segundo valor: '))

    elif opção == 5:
        print('Finalizado...')
    else:
        print('Opção invalida, informe novamente!')
    print('=-=' * 10)
print('Fim do programa!! Volte sempre!!')

