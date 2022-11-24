'''crie um programa que leia varios numeros inteiros
 e so pare quando o usuário digitar 999
 no final mostre quantos foram digitados e
 qual a soma deles.'''

n = s = c = 0

while True:
    n = int(input('Digite um número (999 para parar): '))
    if n == 999:
        break
    c = c + 1
    s = s + n
print(f'A soma foi {s} e foram digitados {c} números.')

