'''
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa mostre: 
A media de idade do grupo 
Qual o nome do homem mais velho 
Quantas mulheres tem menos de 20 anos 
'''
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
'''
#Guanabara

somaidade = 0 
médiaidade = 0
maioridadehomem = 0
nomevelho = 0
totmulher20 = 0
for p in range (1, 5):
    print('----- {} ° PESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade <20:
        totmulher20 += 1
médiaidade = somaidade /4 
print('A média de idade do grupo é de {} anos'.format(médiaidade))
print('O homem mais velho tem {} anos e se chama {}.'.fomrat(maioridadehomem, nomevelho))
print('Ai tidi são {} mulheres com menos de 20 anos.'.format(totmulher20))