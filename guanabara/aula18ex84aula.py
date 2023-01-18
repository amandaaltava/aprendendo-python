'''
Programa que leia nome e peso de várias pessoas numa lista e mostre:
Quantas pessoas foram cadastradas,
 uma listagem com as mais pesadas,
  uma listagem com as mais leves.
'''
cont = mais = menos = tototal = 0
nome = ''
dado = []
lista = []
resp = ''

while True:
    dado.append(input('Nome: '))
    dado.append(input('Peso: '))
    tototal += 1

    resp = (input(f'Quer continuar? [ S / N ]: ')).upper() .strip()[0]
    while resp not in 'SN':
       resp = (input('Digite S para continuar ou N para terminar: ')).upper() .strip()[0]
    if resp == 'N':
        break

for p in dado:
    if p[cont+1]  > mais:
        p[cont+1] = mais
    elif p[cont+1] < menos:
        p[cont+1] = menos
print(f' O peso maior é {mais} e o peso menor é {menos}  ')

'''for cont in range(0, len(dado[::2])):
    if cont == 0:
        mais = menos = dado[cont]
    else:
        if dado[cont] > mais:
            mais = dado[cont]
        if dado[cont] < menos:
            menos = dado[cont]


print(f'O maior peso digitado foi {mais} por ', end='')
for nome, peso in enumerate(dado):
    if peso == mais:
        print(f'{nome} ', end='')

print('')
print(f'O menor peso digitado foi {menos} por ', end='')
for nome, peso in enumerate(dado):
    if peso == menos:
        print(f'{nome}', end='')'''

print('')
print(f'Ao todo você cadastrou {tototal} pessoas.')

