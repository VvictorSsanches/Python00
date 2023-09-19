#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

#Valor
v = float(input('Preço do produto: '))
#vd = Valor do desconto 
vd = v * 0.05
#vcd valor com o desconto aplicado
vcd = v *0.95
print('Valor do pruduto: {}'.format(v))
print('Valor do desconto: {}'.format(vd))
print('Valor com 5% de desconto aplicado: {:.2f}'.format(vcd))

#Ou

v=float(input('Preço do produto'))
print('valor do desconto', v*0.05)
print('valor com o desconto', v*0.95 )

#ou

preço = float(input('Qual o valor do produto? R$:'))
novo = preço - (preço * 5 / 100)
valor_desconto = preço * 5 /100
print('O produto custa R$:{} o valor descontado de 5% é R$:{}, o valor a pagar com o desconto é de R$:{}'.format(preço, valor_desconto, novo))
