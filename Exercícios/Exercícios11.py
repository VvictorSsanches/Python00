#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinra necessária para pinta-lá,
#sabemos que cada litro de tinta, pinta uma área de 2m².

L = float(input('Qual a largura da parede para pintar?: '))
A = float(input('Qual a altura da parede para pintar?: '))
LA = L*A
T = LA / 2

print('Sua parede tem a dimensão de {} x {} e a sua área é de {}m²'.format(L,A,LA))
print('Será necessário um total de {}l de tinta para pintar a prede. '.format(T))


