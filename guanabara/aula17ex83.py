'''Programa que lê uma expressão qualquer que use parênteses.
Seu programa deverá analisar se a expressão está com os parênteses
abertos e fechados e na ordem certa.
'''

expr = input('Digite sua expressão: ')
lista = []
for simbolo in expr:
    if simbolo == '(':
        lista.append('(')
        print(lista)
    elif simbolo == ')':
        if len(lista) > 0:
            lista.pop()
            print(lista)
        else:
            lista.append(')')
            print(lista)
            break
if len(lista) == 0:
    print(lista)
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')

