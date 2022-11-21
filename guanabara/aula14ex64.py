'''crie um programa que leia varios numeros inteiros
 e so pare quando o usuário digitar 999
 no final mostre quantos foram digitados e
 qual a soma deles.'''
c = 1
n = 0
soma = n


while n != 999:
    n = int(input('Digite o número 999 para parar: '))
    c = c +1
    soma += n

print('Parou!')
print(f'Voce digitou {c} números, e a soma deles foi {soma - 999}')



