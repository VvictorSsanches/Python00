'''
Faça um programa que calcule a soma entre todos os números impares que são multiplos de tres e 
que se encontram no intervalo de 1 até 500

'''
'''
for a in range(1, 500):
    if a %2 ==0:
        print()
    else:
        print(a)
'''
s = 0 
for num in range (1,501):
    if num % 2 != 0:
        if num % 3 != 0:
            s += num        
print('A soma dos múltiplos é: {}'.format(s))

s = 0
con = 0
for c in range (1, 501, 2):
    if c % 3 == 0:
        s = s + c
    con = con +1
print('A soma de todos os {} valores solicitados é {}'.format(con, s ))