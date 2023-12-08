'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitado o valor 999, que é a condição
de parada. No final, mostrequantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).'''


s = n = c = 0

while n != 999:
    n = int(input('Informe o valor: '))
    if n == 999:
        break
    c += 1
    s += n 

print ('Números informados {}'.format(c))
print ('Soma dos números informados {}'.format(s))