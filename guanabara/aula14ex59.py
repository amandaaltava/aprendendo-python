'''Programa que leia dois valores e mostre um menu na tela:

[1]somar
[2]multiplicar
[3]maior
[4]novo numeros
[5]sair do programa
o programa devera realizar a operação solicitada em cada caso
'''

from random import randint
from time import sleep

print('*-' * 10)
opcao = ''
print('\033[1;32mMe dê dois valores\033[m')
val1 = float(input('Valor 1: '))
val2 = float(input('Valor 2: '))

while opcao != 5:
    print('Agora escolha qual ação vc quer que executar de acordo com o menu:')
    opcao = int(input('[1]somar [2]multiplicar [3]maior [4]novo numero [5]sair do programa: '))

    if opcao==1:
        soma = val1 + val2
        print(f'\033[7mO valor da soma entre {val1} e {val2} é: {soma}\033[m')

    elif opcao ==2:
        multi = val1 * val2
        print(f'\033[7mO valor da multiplicação entre {val1} e {val2} é {multi}\033[m')

    elif opcao ==3:
        print(f'\033[7mO valor maior entre {val1} e {val2} é {max(val1, val2)}\033[m')

    elif opcao ==4:
        print('\033[1;32mMe dê dois valores\033[m')
        val1 = float(input('Valor 1: '))
        val2 = float(input('Valor 2: '))

    elif opcao ==5:
        print('\033[1mOk, tchau tchau!\033[m')

    else:
        print('Opção inválida')
        sleep(2)
print('Fim do programa.')