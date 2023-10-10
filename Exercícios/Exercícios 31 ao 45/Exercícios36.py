'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa, O programa vai perguntar o valor
da casa, o salário do comprador e em quantos anos ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ela não pode exeder 30% do salário ou então o emprestimo será negado
'''

vcasa = float(input('Informe o valor da casa: '))
salario = float(input('Informe o salário: '))
anos = int(input('Informe o tempo quantos anos para pagar a casa '))
pmensal = vcasa / anos * 12
porcetagem = pmensal * 100 / salario

if pmensal <=0.3 *salario:
        
    print('O pagamento mensal do imovel é de {:.2f} \nPara o emprestimo ser aprovado o pagamento mensal'
          ' não deve ser superior a 30% do salário do individuo. O resultado foi: {:.2f}% \nSeu emprestimo foi'
          ' \033[1;32maceito\033[m'
          ' Parabéns'.format(pmensal,porcetagem))
else:
    
    print('O Pagamento mensal do imovel é de {:.2f} \nPara o emprestimo ser aprovado o pagamento mensal'
          'não deve ser superior a 30% do salário do individuo. O resultado foi: {:.2f}% \nSeu emprestimo foi'
          ' \033[1:31Negado\033[m'
          ' Desculpe'.format(pmensal,porcetagem))