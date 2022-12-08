'''Programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
No final mostre
quantas vezes o valor 9 apareceu
em que posição foi digitado pela primeira vez o número 3
quais foram os números pares'''
cont = 0

tupla = (int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')))
print(f'Você digitou os números: {tupla}')
print(f'O valor 9  aparece {tupla.count(9)} vezes.')
if 3 in tupla:
    print(f'O número 3 foi digitado pela primeira vez na {tupla.index(3)+1}ª posição .')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
print('Os valores pares digitados foram:')
for n in tupla:
    if n % 2 == 0:
        print(n, end='')

leia quatro valores pelo teclado e guarde-os em uma tupla. No final mostre quantas vezes o valor 9 apareceu em que posição foi digitado pela primeira vez o número 3 quais foram os números pares