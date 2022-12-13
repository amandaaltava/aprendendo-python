'''Programa que tenha uma tupla unica com os nomes de produtos e seus respectivos preços na sequencia
No final mostre uma listagem  de preços organizados em forma tabular - tabela'''

print(',,'*20)
print(f'{"LISTAGEM DE PRODUTOS":^30}')
print(',,'*20)

produtos = ('Maça', 1.00, 'Abacaxi', 3.00, 'Banana', 2.50, 'Kiwi', 4.00, 'Morango', 2.50, 'Manga', 2.89, 'Melao', 4.00, 'Melancia', 6.00, 'Mamao', 3.00)

for posicao in range(0, len(produtos)):
    if posicao % 2 == 0:     # vai pegar a posição de índex dos itens na tabela e saber se for par é produto se for ímpar é preço
        print(f'{produtos[posicao]:.<30}', end='')
    else:                    # vai pegar a posição de índex dos itens na tabela e saber se for ímpar é o preço
        print(f'R$ {produtos[posicao]:>.2f}')