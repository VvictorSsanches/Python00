print('\033[4;31;43m Olá Mundo!\033[m')
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33',
         'vermelho': '\033[34',
         'brancoepreto': '\033[7:30'}

nome = 'Victor'
print('Olá! Prazer em conhecer você {}{}{}'.format(cores ['azul'], nome, cores ['limpa'] ))
print('Olá! Muito prazer em lhe conhecer {}{}{}'.format('\033[4;31;44m', nome, '\033[m'))