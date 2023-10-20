peso = float(input('Qual o seu peso? (Kg) '))
altura = float(input('Qual a sua altura? (m) '))
imc = peso / (altura **2)
if imc <18.5:
    print('Seu IMC é de {:.2f}. Você está abaixo do peso.'.format(imc))
elif 18.5 <= imc < 24.9:
    print('Seu IMC é de {:.2f}. PARABENS, você está na faixa de PESO NORMAL.'.format(imc))
elif 25 <= imc < 29.9:
    print('Seu IMC é de {:.2f}. Você está sobrepesso.'.format(imc))
elif  30 <= imc < 34.9:
    print('Seu imc é de {:.2f}. Você está com OBESISADE GRAU 1.'.format(imc))
elif 35 <= imc < 39.9:
    print('Seu Imc é de {:.2f}. Você está com OBESIDADE GRAU 2.'.format(imc))
else:
    print('Seu Imc é de {:.2f}. Você está com OBESIDADE GRAU 3.'.format(imc))
