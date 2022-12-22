'''
Programa que o usuário insere 5 valores numéricos e
os cadastre em um lista já na posição correta
sem usar o sort(). No final mostre a lista ordenada na tela
'''

lista = list()
for c in range(0, 5):
    v = int(input(f'Insira o {c} valor: '))
    if c == 0 or v > lista[-1]:
        lista.append(v)
        print('Valor adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if v <= lista[pos]:
                lista.insert(pos, v)
                print(f'Adicionado na {pos} da lista')
                break
            pos = pos + 1
print('*'*30)
print(f'A lista completa é {lista}')

Programa que o usuário insere 5 valores numéricos e os cadastre em um lista já na posição correta sem usar o sort(). No final mostre a lista ordenada na tela