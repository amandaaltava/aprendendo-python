'''Faça um programa que leia um número inteiro e mostra se é PAR ou ÍMPAR'''

from time import sleep   #importa a função sleep da biblioteca time

num = int(input('Insira um número e te direi se é PAR ou ÍMPAR:'))
resultado = num % 2     # % é o símbolo de resto da divisão, se for 0 é par se for 1 é ímpar
sleep(1)     #espera alguns instantes para aparecer novamente o progama
if resultado == 0:
    print('Seu número é PAR!')
else:
    print('Seu número é IMPAR!')
