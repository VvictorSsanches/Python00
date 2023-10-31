'''
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa mostre: 
A media de idade do grupo 
Qual o nome do homem mais velho 
Quantas mulheres tem menos de 20 anos 
'''

soma = 0
cont_mulheres = 0
media = 0
maior = 0
NomeHomensMaisVelhos = ''

for cont in range(1,4):
    nome = str(input('digite seu nome: '))
    sexo = str(input('Masculino ou Feminino? [M/F]: ')).upper()
    while sexo :
        if sexo != 'M' and sexo != 'F':
            print('Tente novemente')
            sexo = str(input('Masculino ou Feminino? [M/F]: ')).upper()
    idade = int(input('Digite sua idade: '))
    print('-'*20)

    soma = soma + idade
    media = soma / cont

    if sexo == 'M' and idade > maior:
        maior = idade
        NomeHomensMaisVelhos = nome

    if sexo == 'F' and idade <20:
        cont_mulheres +=1

print('Media das idade é de {:.2f}'.format(media)) 
print('Nome do mais velho é {}'.format(NomeHomensMaisVelhos))

if cont_mulheres == 0:
    print('Não Temos Mulheres no grupo !')

else:
    print('A todo temos {} mulheres com menor de 20 anos'.format(cont_mulheres))