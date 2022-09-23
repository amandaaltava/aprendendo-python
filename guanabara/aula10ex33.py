'''Faça um programa que leia três números e diga qual é o maior e o menor deles.'''

'''n1 = float(input('Insira um número:'))
n2 = float(input('Insira outro número: '))
n3 = float(input('Insira um último número:'))
maior = max(n1, n2, n3)
print('{} é o maior'.format(maior))
menor = min(n1, n2, n3)
print('{} é o menor.'.format(menor))'''

a = int(input('Digite um valor:'))
b = int(input('Digite um valor: '))
c = int(input('Digite um valor: '))
# verificando quem é o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
    # verificando quem é o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))
