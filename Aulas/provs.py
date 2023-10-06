import math

print('-=-'*10)
('Divisão inteira e Resto da divisão')
print('-=-'*10)
a = float(input('Primeiro número: '))
b = float(input('Segundo Número: '))
r = (a // b)
R = (a % b)
print('Valor da divisão inteira é:{}\nResto da divisão é:{}'.format(r,R))

  # fazer o mmc 
'''
n1 = float(input('Informe o primeiro valor: '))
n2 = float(input('Informe o segundo valor: '))

if n1 > n2:
    maior = n1
else:
    maior = n2
while True:
    if maior % n1 == 0 and maior % n2 == 0:
        print(maior)
        break       
    else:
      maior +=1
'''

num1 = int(input("Digite um número inteiro:"))
num2 = int(input("Digite outro número inteiro:"))

if num1 > num2:
    maior = num1
else:
    maior = num2

for i in range(maior):
    aux = num1 * i
    if (aux % num2) == 0:
        mmc = aux

print(mmc)

