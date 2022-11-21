'''Faça um programa que os exiba os termos finobacci
e pergunte se o usuário quer exibir mais termos'''

n = int(input('Digite um número e te mostrai sua sequência fibonacci: '))
t1 = 0
t2 = 1
print(f'{t1} ¬ {t2}', end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(f' ¬ {t3}', end='')
    t1 = t2
    t2 = t3
    cont = cont + 1
print(' Fim')
