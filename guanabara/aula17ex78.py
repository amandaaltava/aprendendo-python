'''Programa que leia 5 valores numéricos e guarde em uma lista.
No final mostre qual foi o maior e o menor valor digitado
e as suas respectivos posições na lista'''

maior = 0
menor = 0

lista = []
for cont in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {cont}: ')))
    if cont == 0:
        maior = menor = lista[cont]
    else:
        if lista[cont] > maior:
            maior = lista[cont]
        if lista[cont] < menor:
            menor = lista[cont]

print('+'*30)
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}...', end='')



'''   - Funciona, mas não varre a lista toda
lista = []
for cont in range(0, 5):
    lista.append(int(input(f'Digite um valor {cont}: ')))
maximo = max(lista)
minimo = min(lista)

pos = lista.index(maximo)
pos1 = lista.index(minimo)


print('-='*10)
print(f'Você digitou os valores {lista}')
print(f'Valo maximo {maximo}  o índice {pos}')
print(f'Valo maximo {minimo}  o índice {pos1}') '''



Programa que leia 5 valores numéricos e guarde em uma lista. No final mostre qual foi o maior e o menor valor digitado e as suas respectivos posições na lista