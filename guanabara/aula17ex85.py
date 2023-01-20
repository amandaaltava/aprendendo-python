'''Crie um programa onde o usuário possa digitar 7 valores
numéricos e cadastreos em uma lista única, que mantenha
separados os valores pares dos ímpares. No final mostre
os valores pares e os ímpares em ordem decrescente'''
listaprin =[[], []]
num = result = 0

# Capta em loop os valores inseridos
for c in range(1, 8):
    num = (int(input(f'Digite o {c}º valor:')))  # Posso usar o 'c' como contador direto pq iniciei o range em 1 e não 0.
    if num % 2 == 0:           # Se o resto da divisão for 0 é par
        listaprin[0].append(num)    # Adiciona na lista par que é a posição 0 da lista principal
    else:
         listaprin[1].append(num)    # Adiciona na lista ímpar que é a posição 1 da lista principal

listaprin[0].sort()      # Ordena em ordem crescente a posição [0]
listaprin[1].sort()      # Ordena em ordem crescente a posição [1]

print(listaprin[0])
print(listaprin[1])


Crie um programa onde o usuário possa digitar 7 valores numéricos e cadastreos em uma lista única, que mantenha separados os valores pares dos ímpares. No final mostre os valores pares e os ímpares em ordem decrescente