'''Crie um programa que leia números no teclado, pergunte se o usuário que continuar
no final mostre a média de todos o maior e o menor deles'''

n = 0
media = 0
c = 0
p = 's'
s = 0
ma = 0
mi = 0


print('Digite um número e digite S para continuar e N para parar.')
while p in 'Ss':
    n = int(input('Digite um número inteiro: '))
    c = c +1
    s += n
    if c == 1:
      ma = mi = n
    else:
      if n > ma:
          ma = n
      if n < mi:
          mi = n
    p = str(input('Se deseja continuar digite "S", se quer parar digite "N": ')).upper().strip()[0]

print(f'soma é {s} e digitou tantos {c} maximo {ma} e minimo {mi}')

   # media = soma / c