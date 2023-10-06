nome = str(input('Qual é o seu nome: '))
if nome == 'João'.lower():
    print('Que nome bonito')
    
# Pode se usar para ver nomes expecificos.
elif nome == 'Jose'.lower() or nome == 'Pedro'.lower() or nome == 'Gabriel'.lower():
    print('Seu nome é bem popular')
# Ver nomes que podem ser escritos, não seria uma lista necessáriamente.
elif nome in 'Matheus Victor Paulo Gilberto Felipe'.lower():
    print('Você tem um belo nome')

else:

    print('Que nome normal')

print('Tenha um bom dia {}'.format(nome))