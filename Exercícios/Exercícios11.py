#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinra necessária para pinta-lá,
#sabemos que cada litro de tinta, pinta uma área de 2m².

L = float(input('Qual a largura da parede para pintar?: '))
A = float(input('Qual a altura da parede para pintar?: '))
LA = L*A
T = 2**2
TO = LA*T
print('Será necessário um total de {} litros de tinta para pintar a prede. '.format(TO))


