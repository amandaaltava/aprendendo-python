'''Programa qye  leia o nome e o preço de varios produtos e deverá perguntar se
o usuário que continuar. No final deve mostrar:
qual é o gasto total, quantos produtos custam mais de MIL reais
que é o NOME no produto mais barato'''

cont = 0
cmaior = 0
menor = 0
nmenor = ' '
preco = 0
soma = 0

while True:
    print('='*20)
    print('LOJA DO VEIO DA VAN')
    print('Cadastre o Produto')
    print('='*20)
                                #Input dos dados
    produto = str(input('Nome do Produto:'))
    preco = float(input('Preço do Produto: R$ '))
    cont = cont + 1              #Contador para saber se é o menor preço e fazer a atribuição para posterior eventual substituição do valor menor
    soma = soma + preco
                                 #Condição para saber se é maior que mil
    if preco > 1000:
            cmaior = cmaior +1
                                  #Checa se é o menor preço atrubuindo a variavel e depois verificando se o valor novo é menor e então substitui
    if cont == 1 or preco < menor:
        menor = preco
        nmenor = produto

    tipo = ' '           #Limpando a variavel da escolha
    while tipo not in 'SN':
        tipo = str(input('Deseja continuar? [S / N]:')).strip().upper()[0]
    if tipo == 'N':
            break
                                #Entregando o resultado
print(f'O total da compra foi {soma:.2F}.')
print(f'Temos {cmaior} produtos custando mais que Mil reais.')
print(f'O produto mais barato foi {nmenor} que custou {menor:.2F}')

