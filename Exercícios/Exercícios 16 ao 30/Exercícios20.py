#O mesmo professor do desafio a ordem de apresentação de trabalho dos alunos.
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

a1 = str(input('1° Aluno: '))
a2 = str(input('2° Aluno: '))
a3 = str(input('3° Aluno: '))
a4 = str(input('4° Aluno: '))

lista = [a1, a2, a3, a4]
shuffle(lista)
print('Lista para realizar a apresentação: \n{}'.format(lista))

# OU

lista = ['vitor', 'gabi', 'nath', 'bino']
shuffle(lista)
print('Lista para realizar a apresentação: \n{}'.format(lista))