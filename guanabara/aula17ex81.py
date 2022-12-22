'''
Programa que lê vários números e colocar em uma lista.
Depois disso mostre:
Quantos npumeros foram digitados.
A lista de valores ordenada de forma DECRESCENTE.
Se o valor 5 foi digitado e está ou não na lista.
'''

lista = list()
while True:
    lista.append(input('Digite um valor: '))   #Adiciona o valor na lista

    resp = str(input('Deseja continuar? [ S / N ]: ')).upper().strip()
    while resp not in 'SN':                              #Verifica se o digitado foi mesmo a opção solicitada.
        resp = str(input('Você não digitou corretamente. Deseja continuar ? [ S / N ]: ')).upper().strip()
    if resp == 'N':
        break

print('..'*20)
print(f'Você digitou {len(lista)} itens') #Len trás o tamanho da lista

lista.sort(reverse=True)   #Coloca a lista em ordem decrescente
print(f'Você digitou os seguintes valores em ordem decrescente {lista}')

if '5' not in lista:          #Procura o 5 na lista
    print('O número 5 NÃO foi encontrado.')
else:
    print(f'O 5 foi encontrado')


Programa que lê vários números e colocar em uma lista. Depois disso mostre: Quantos npumeros foram digitados. A lista de valores ordenada de forma DECRESCENTE. Se o valor 5 foi digitado e está ou não na lista.