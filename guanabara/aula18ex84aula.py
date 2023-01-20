'''
Programa que leia nome e peso de várias pessoas numa lista e mostre:
Quantas pessoas foram cadastradas,
 uma listagem com as mais pesadas,
  uma listagem com as mais leves.
'''
temp = []
princ = []
tototal = 0
mai = men = 0

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
# ele vai pegar cada dado que entra no temp[1] que é o peso e já vai comprarar para ver se é o
# maior ou menor e guardar em uma variável. Ou seja, já tenho a informação fora da lista
# de quem é o maior ou menor
    if len(princ) == 0:       # Se eu ainda não tiver cadastrado ninguém, ou seja o tamanho da principal é 0
        mai = men = temp[1]   # temp [1] é o item na posição 1, que é o peso
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]

    princ.append(temp[:])
    temp.clear()
    print(temp, princ)
    resp = (input(f'Quer continuar? [ S / N ]: ')).upper() .strip()[0]
    while resp not in 'SN':
       resp = (str(input('Digite S para continuar ou N para terminar: '))).upper() .strip()[0]
    if resp == 'N':        #(também pode ser '  in not 'Nn'  )
        break
    tototal += 1    #(pode também não fazer um contador, pode usar o tamanho de itens na lista principal com o len>> len(princ)

print('...' * 20)
print(f'Ao todo vc cadastrou {tototal} pessoas.')


# Agora o for vai varer cada lista dentro da lista princ pegando o item p[1] que é o peso
# e vai comparar com a informação que eu já guardei na variável fora da lista lá no inicio
# Quando o valor for igual da variável, ele vai pegar o item anterior da lista em que ele estiver, no caso, p[1]
print(f'O maior peso foi de {mai}kg. Peso de', end='')
for p in princ:
    if p[1] == mai:
        print(f' {p[0]}', end='')  #item anterior ao p[1]

print()
print(f'O menor peso foi de {men}kg. Peso de ', end='')
for p in princ:
    if p[1] == men:
        print(f'Peso de {p[0]}', end='') #item anterior ao p[1]

Programa que leia nome e peso de várias pessoas numa lista e mostre: Quantas pessoas foram cadastradas, uma listagem com as mais pesadas, uma listagem com as mais leves