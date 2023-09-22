import random

sorteio = [ 'PEDRA','PAPEL','TESOURA' ]
escolha=str(input('Você quer pedra, papel ou tesoura: ')).upper()
j=sorteio [random.randrange(len(sorteio))]

if escolha== j:
    print(f'Você escolheu {escolha} e seu PC escolheu esse {j}')
    print('Jogue de novo')
#PC ganha
elif escolha=='PEDRA' and j=='PAPEL':
    print (f'Você escolheu {escolha} e seu PC {j}!! Pc ganhou essa')
elif escolha =='PAPEL' and j=='TESOURA':
    print (f'Você escolheu {escolha} e seu PC {j}!! Pc ganhou essa')
elif escolha=='TESOURA' and j=='PEDRA':
    print (f'Você escolheu {escolha} e seu PC {j}!! Pc ganhou essa')
#Vc ganha
elif escolha=='PAPEL' and j=='PEDRA':
    print (f'Você escolheu {escolha} e seu PC {j}!! VC ganhou essa')
elif escolha =='TESOURA' and j=='PAPEL':
    print (f'Você escolheu {escolha} e seu PC {j}!! VC ganhou essa')
elif escolha=='PEDRA' and j=='TESOURA':
    print (f'Você escolheu {escolha} e seu PC {j}!! VC ganhou essa')
#qual quer coisa que não for as três opções cai aqui
else:
    print('Escolha uns das opções')