'''Faça um progama que calcule um preço de venda de um produto e considerer o seu preço normal e as
seguintes condições de pagamento:
a vista no dinheiro ou cheque 10% desc
a vista no cartao 5% desc
em até 2x no cartao preço normal
3x ou mais no cartao 20% juros'''

pre = float(input('Insira o preço R$  '))
cond = int(input('''Qual será a condição de pagamento:'
                 'a vista [1]'
                 'a vista no cartão[2]'
                 'até 2x no cartão [3]'
                 '3x ou mais no cartão [4]: '''))

if cond == 1 :
    print(f'A condição de pagamento será em dinheiro. Então você terá 10% de desconto, o valor será {pre - (pre * 0.10)}.')
elif cond == 2 :
    print(f'A condição de pagamento a vista no cartão. Então você terá 5% de desconto, o valor será {pre - (pre * 0.05)}.')
elif cond == 3 :
    print(f'A condição de pagamento é até 2x no cartão, cada parcela é de R$ {pre / 2 :.2f}. Então o preço será R${pre :.2f} .')
elif cond == 4 :
    parcelas = int(input('Quantas parcelas?'))
    parcela = ((pre + (pre * 0.20))/ parcelas )
    print(f'O preço do produto é {pre :.2f} e a condição de pagamento é em {parcelas} x ou mais no cartão, cada parcela no valor de R$ {parcela :.2f} . Então o preço será R${pre + (pre * 0.20) :.2f}. ')
else:
    print('Opção inválida')