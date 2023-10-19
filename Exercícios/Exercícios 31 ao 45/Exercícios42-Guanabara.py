a1 = float(input('Insira o primeiro comprimento: '))
a2 = float(input('Insira o segundo comprimento: '))
a3 = float(input('insira o terceiro comprimento: '))

if a2 + a3 > a1 and a2 + a1 > a3 and a1 + a2 > a3:
    print('O tiangulo mexiste.')
    if a1 == a2 and a1 != a3:
        print('ela é Equilátero.')
    elif a1 != a2 and a1 != a3:
        print('ela é Escaleno.')
    else:
        print('ela é Isósceles.')
else:
    print('O Triangulo não existe.')