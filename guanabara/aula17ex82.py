'''Programa que vai ler vários números e colocar em uma lista.
Depois disso crie duas listas extras, uma com os numeros pares e outra com os ímpares.
Ao final mostre as três listas
'''

# Inicia as listas que serão usadas
lista = list()
lista2 = list()
lista3 = list()

while True:
    lista.append(int(input('Digite um valor: ')))   #Input dos valores
    resp = str(input('Deseja continuar? [ S / N ]: ')).upper().strip()
    while resp not in 'SN':                           #Verificação da resposta
        resp = str(input('Você não digitou corretamente. Deseja continuar: [ S / N]: ')).upper().strip()
    if resp == 'N':
        break

print('--' * 20)
lista.sort()      # Coloca os itens em ordem para facilitar a vizualização da lista
print(f'Digitou: {lista} ')

for c in range(0, len(lista)):   # Varre a lista de 0 até o final
    if lista[c] % 2 == 0:        # Condição de par e ímpar
        lista2.append(lista[c])  # Adiciona na lista par
    else:
        lista3.append(lista[c]) # Adiciona na lista ímpar


print(f'Lista par {lista2}')
print(f'Lista ímpar {lista3}')

