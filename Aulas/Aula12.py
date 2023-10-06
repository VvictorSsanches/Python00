# Condicionais Aninhadas
# if elif e else

'''
if = se 
elif = senão
else = mais


'''

'''
carro.siga()

se carro.esquerda()
    carro.siga()
    carro.esquerda()
    carro.siga()
    carro.direita()
    carro.siga()
    carro.direita()
    carro.siga()
    carro.esquerda()
    carro.siga()

senão se carro.direita()
    carro.siga()
    carro.esquerda()
    carro.siga()
    carro.esquerda()
    carro.siga()

senão
    carro.siga()
Carro.pare()    
    '''

carro.siga()

if carro.esquerda():
    carro.siga()
    carro.esquerda()
    carro.siga()
    carro.direita()
    carro.siga()
    carro.direita()
    carro.siga()
    carro.esquerda()
    carro.siga()

elif carro.direita():
    carro.siga()
    carro.esquerda()
    carro.siga()
    carro.esquerda()
    carro.siga()

else:
    carro.siga()
Carro.pare()    