'''Faça um programa para aprovar um empréstimo bancário para a compra
de uma casa. O programa vai perguntar o valor da casa, o salário
do comprador e em quantos anos ele vai pagar.

calcule o valor da prestação mensal, sabendo que ela não
pode exceder 30% do salário se não o empréstimo será negado.'''

from time import sleep

print('\033[4;35m---\033[m' * 12)
print('\033[1;32;40m   Vamos calcular o seu empréstimo. \033[m')
print('\033[4;35m---\033[m' * 12)

# recebendo as informações do usuário
salario = float(input('\033[33;40m Digite o valor do seu salário R$ \033[m'))
casa = float(input('\033[33;40m Digite o valor da casa R$ \033[m'))
anos = int(input('\033[33;40m Digite em quantos anos que você quer pagar essa casa: \033[m'))
mensalidade = (casa / anos) / 12


# Interagindo com o usuário
print('\033[1;35;40m CERTO, VOU CALCULAR PARA VOCÊ AGORA.')
sleep(1)
print('\033[1;32;40m CALCULANDO... \033[m')
sleep(2)
print(f'\033[1;33;40m Sua parcela será de R$ {mensalidade:.2f}. \033[m')
sleep(2)

# calculando se o empréstimo vai ou não ocorrer
if mensalidade < salario * 0.30:
    print('\033[1;97;42m PARABÉNS, SEU EMPRÉSTIMO FOI APROVADO! \033[m')
else:
    print('\033[1;31;40m DESCULPE, MAS SEU EMPRÉSTIMO FOI NEGADO! \033[m')

print('\033[1;97;41m Vote melhor na próxima eleição! \033[m')