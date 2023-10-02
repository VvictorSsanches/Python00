'''
escreva um programa que leia a velocidade de um carro 
se ele ultrapassar 80km/h, moste uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite

'''
'''
velo = float(input('informe a sua velocidade: '))
multa = (velo -80) * 7
if velo <= 80:
    print('Você não levou multa!')
else:
    print('A sua velocidade foi de {}Km/h \nVocê vai ser multa em R$: {}'.format(velo, multa))

'''
velocidade = int(input('Informe a velocidade: '))

if velocidade > 80:
    print('Você execeu o limite da via, limite permitido de 80km/h.')
    multa = (velocidade - 80)*7
    print('Sua multa sera de R$: {}.'.format(multa))
print('Tenha um excelente dia, dirija com cuidado.')