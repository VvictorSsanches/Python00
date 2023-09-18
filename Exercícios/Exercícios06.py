#Crie um algoritimo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
'''
x = int(input('Insira um valor: '))
n1 = x * 2
n2 = x * 3
n3 = x ** (1/2)
print('O valor inserido foi {} \nO dobro dele é: {} \nO triplo é: {} \nA raiz ao quadrado é: {5}.'.format(x, n1, n2, n3))
'''
#Ou

x = int(input('Insira um valor: '))
print('O valor inserido foi {} \nO dobro dele é: {} \nO triplo é: {} \nA raiz ao quadrado é: {:.2f}'.format(x, (x*2), (x*3) ,(x **(1/2))))

#ou

x = int(input('Insira um valor: '))
print('O valor inserido foi {} \nO dobro dele é: {} \nO triplo é: {} \nA raiz ao quadrado é: {:.2f}'.format(x, (x*2), (x*3) ,pow(x ,(1/2))))
