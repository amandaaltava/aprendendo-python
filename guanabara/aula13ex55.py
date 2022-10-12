'''Faça um programa que leia o peso de cinco pessoas
no final mostre qual foi o maior e o menor peso lidos'''

# duas formas de colocar os dados do input em uma lista para análise na segunda linha
''' peso = [input('Digite o peso da pessoa: ') for laco in range(0, 5)]
print(f'O maior peso foi {max(peso)}, e o menor peso foi {min(peso)}')

nomes = [str(input('Digite o nome: ')) for laco in range(0,5)]
print('a ordem dos nomes é {}'.format(sorted(nomes))) '''

maior = 0
menor = 0

for p in range(1, 6):
    peso = float(input('Peso da {}º pessoa: ' .format(p)))
    if p == 1:
        maior = p
        menor = p
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}Kg.' .format(maior))
print('O menor peso lido foi de {}kg.' .format(menor))
