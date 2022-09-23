import random

n1 = str(input('Insira o nome do aluno: '))
n2 = str(input('Insira o nome do aluno: '))
n3 = str(input('Insira o nome do aluno: '))
n4 = str(input('Insira o nome do aluno: '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem de alunos será:{} '.format('\033[31m', lista[0], '\033[m'))
