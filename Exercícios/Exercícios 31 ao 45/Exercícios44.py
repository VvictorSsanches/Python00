'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal
e condição de pagamento: - à vista dinheiro/cheque: 10% de desconto - à vista no cartão: 5% de
desconto - em até 2x no cartão: preço formal - 3x ou mais no cartão: 20% de juros
'''
valor = float(input('Valor do produto: '))

escolha = int(input('[1] Dinheiro/cheque 10% de desconto'
                    '\n[2] À Vista no cartão 5% de desconto'
                    '\n[3] Até 2x no cartão'
                    '\n[4] À cima de 3x no cartão 20% de juros'
                    '\nInforme a opção: '))

if escolha == 1:
    print('O descomnto com 10% é de {:.2f}R$ o valor irá ser de {:.2f}R$.'.format(valor *0.10,valor*0.90))
elif escolha == 2:
    print('O desconto com 5% é de {:.2f}R$ o valor irá ser de {:.2f}R$.'.format(valor*0.05,valor*0.95))
elif escolha == 3:
    print('O valor até 2x será de {:.2f} será o valor de {:.2f}R$.'.format(valor / 2,valor))
elif escolha == 4:
    total = valor +(valor * 0.20)
    x = int(input('Quantas parcelas? '))
    parcela = total / x
    print('O produto será parcelado em {}x de {:.1f}R$ COM JUROS \nSua compra de {:.1f}R$ o valor será de {:.1f}.'.format(x, parcela, valor, total ))
else:
    print('Opção invalida \nTENTE NOVAMENTE!!')