'''Programa em que o usuário digita números para
coloca-los numa lista. Se o número digitado já tiver sido inserido
ele não será adicionado. No final serão exibidos os valores adicionados na
lista em ordem crecente'''

lista = []
while True:
    valor = int(input('Digite um valor: '))
    if valor not in lista:
        lista.append(valor)
        print('Valor adicionado com sucesso.')
    else:
        print('Valor duplicado! Não vou adicionar.')
    resp = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if resp == 'N':
        break
lista.sort()
print(f'Seus valore são: {lista}')




