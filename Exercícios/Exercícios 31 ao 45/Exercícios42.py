'''Refaça o DESAFIO 035 dos triângulos (condição de existência), acrescentando o recurso de mostrar
que tipo de triângulo será formado: - EQUILÁTERO: todos os lados iguais - ISÓSCELES: dois lados
iguais, um diferente - ESCALENO: todos os lados diferentes
'''
print('-=-'*20)
print('Analisador de Triangulos')
print('-=-'*20)

a1 = float(input('Insira o primeiro comprimento: '))
a2 = float(input('Insira o segundo comprimento: '))
a3 = float(input('insira o terceiro comprimento: '))

if a2 + a3 > a1 and a2 + a1 > a3 and a1 + a2 > a3:
    print('O tiangulo mexiste.')
    if a1 == a2 and a1 != a3:
        print('ela é Equilátero.')
    elif a1 != a2 and a1 != a3:
        print('ela é Escaleno.')
    elif a1 == a2 and a1 != a3 and a1 == a3 and a1 != a2 and a2 == a3 and a2 != a1:
        print('ela é Isósceles.')
else:
    print('O Triangulo não existe.')
