'''
carro = int(input('Quantos tem o seu carro?: '))
if carro <=3:
    print('Carro novo')
else:
    print('Carro velho')
print('--FIM--')
'''
'''
nome = str(input('Qual o seu nome?'))
if nome == 'Victor'.lower() :
    print('Que nome lindo você tem!')
else:
    print('seu nome é tão normal')
print('Bom dia, {}'.format(nome))
'''
'''
n1 = int(input('Insira a sua primeira nota: '))
n2 = int(input('Insira a sua segunda nota: '))
m = (n1 + n2) / 2
print('A sua média fiu {:.1f}'.format(m))
if m >+ 6.0:
    print('Sua média foi boa!! PARABÉNS')
else:
    print('Sua média foi ruim!!!! ESTUDE MAIS!!')
'''
n1 = float(input('insira sua primeira nota: '))
n2 = float(input('Insira sua segunda nota: '))
m = (n1 + n2) / 2
print('A sua média foi {:.1f}'.format(m))
print('sua média foia boa!!' if m >= 6.0 else 'Sua média foi ruim')



