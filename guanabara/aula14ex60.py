'''Programa que leia um numero qualquer e mostre seu fatorial'''

from time import sleep
'''n = int(input('Insira um número inteiro: '))
c = n
f = 1
print(f'Calculando {n}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')'''

'''from math import factorial
n = int(input('Digite um número: '))
f = factorial(n)
print(f'O fatorial é {f}')'''

n = int(input('Insira o número para fatorar: '))
f = 1
print(f'Calculando {n}! = ', end='')
for c in range(n, 0, -1):
    print(f' {c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f = f * c
print(f'{f}')
