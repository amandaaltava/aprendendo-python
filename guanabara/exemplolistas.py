lista = ['Bala', 'Biscoito', 'Pudim', 'Sorteve']
print(lista)
lista.append('Chocolate')
print(lista)

lista.insert(0, 'Pavê')
print(lista)

del lista[4]
print(lista)

lista.pop(0)
print(lista)

lista.remove('Biscoito')
print(lista)


lista = list(range(4, 11))
print(lista)

lista = [5, 8, 9, 7, 2, 8, 4, 0, 1, 3]
print(lista)

lista.sort()
print(lista)

lista.sort(reverse = True)
print(lista)

print(len(lista))

lista = list()
for cont in range(0, 4):
    lista.append(int(input('digite um valor:')))

for e, l in enumerate(lista):
    print(f'Na posição {e} encontrei o valor {l}!')
print('cheguei ao fim.')

listaa = [  5,   8,   9,   7   ]
listab = listaa [:]
print(listaa)
print(listab)

listab[  2 ] = 0
print(listab)

listaa[0] = 1
print(listab)