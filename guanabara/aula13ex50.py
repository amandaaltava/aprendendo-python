'''Faça um programa que leia 6 números inteiros
e mostre a soma apenas daqueles que forem pares
se o valor digitado for ímpar, desconsidere-o'''

# seta o contador em 0
soma = 0

# seta contador em 0
cont = 0

# laço para pegar os números, conferir e somar
for pares in range(1, 7):
    n = int(input(f'Digite o {pares} número: '))
    if n % 2 == 0:
        soma += n # acumula os numeros que sao verdadeiros no laço
        cont += 1  # conta quantos numeros são verdadeiros no laço

print(f'Você informou {cont} e a soma dos números pares é {soma} .')
