'''Programa que vai gerar cinco números aleatórios
e colocar em uma tupla
Depois mostre a listagem na tela, e também o maior e
o menor números gerados'''

from random import randint

tupla = (randint(0, 5),randint(0, 5),randint(0, 5),randint(0, 5),randint(0, 5),)
print(f'Os números escolhidos foram: {tupla}')
print(f'O número maior foi {max(tupla)}')
print(f'O número maior foi {min(tupla)}')


vai gerar cinco números aleatórios e colocar em uma tupla Depois mostre a listagem na tela, e também o maior e o menor números gerados