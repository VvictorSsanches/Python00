# Faça um algoritmo que leia o salário de um fincionário e mostre seu novo salário, com 15% de aumento.
salário = float(input('qual o salário atual?: '))
aumento = salário + (salário * 15 / 100)
valor_aumento = salário * 15 / 100
print('Valor do salário atual é R$:{:.2f} com o seguinte aumento de R$:{:.2f}, o salário atual é de R$:{:.2f}'.format(salário, valor_aumento, aumento))