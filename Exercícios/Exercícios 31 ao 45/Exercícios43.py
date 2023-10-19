'''
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de
Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo: - IMC abaixo
de 18,5: Abaixo do Peso - Entre 18,5 e 25: Peso Ideal - 25 até 30: Sobrepeso - 30 até
40: Obesidade - Acima de 40: Obesidade Mórbida
'''

peso = float(input('Informe o seu peso: '))
altura = float(input('Informe a sua altura: '))
imc = peso / (altura**2)
print('Seu IMC é de {:.2f}'.format(imc))
if  imc == 18.5: 
    print('Seu IMC é {:.2f} você está abiaxo do peso'.format(imc))
elif imc < 24.9:
    print('Seu IMC é {:.2f} você está no peso normal'.format(imc))
elif imc < 29.9:
    print('Seu IMC é {:.2f} você está sobrepeso'.format(imc))
elif imc < 34.9:
    print('Seu IMC é {:.2f} você está com obesidade Grau 1'.format(imc))
elif imc < 39.9:
    print('Seu IMC é {:.2f} você está com o besidade Grau 2 (Severa)'.format(imc))
else:
    print('Seu IMC é {:.2f} você está com obesidade Grau 3 (mórbida)'.format(imc)) 
