'''
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. 
O programa será interrompido quando o número solicitado for negativo  '''


while True:
    n = int(input('Informe o a tabuada que deseja ver: '))
    print('-' * 30)
    if n < 0:
        break
    for c in range (1 , 11):
        print(f'{n} x {c} = {n*c}') 
    print('-' * 30)
print('Programa da tabuada encerrado. volte sempre!')