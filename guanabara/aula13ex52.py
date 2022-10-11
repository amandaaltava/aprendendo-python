'''Faça um programa que leia um número inteiro
e diga se ele é ou não um número primo

obs: é auqele divisível por 1 e por ele mesmo e nenhum outro até ele'''

n = int(input('Insira o número: '))
c = 0

for primo in range(1, n + 1):   # laço começa de 1 e adiciona 1 ao número
    if n % primo == 0:       # verifica se ele é primo ou não dividindo o número pelo laço
        print('\033[33m', end=' ')   # formata a cor para que o número do laço, receba a cor de acordo com o resultado do IF, ser positivo ou negativo
        c += 1   # contador
    else:
        print('\033[31m', end=' ')
    print(f'{primo}', end=' ')   # imprime o intervalo do laço que parte de 1 até o número e é o IF que

print(f'O número {n} foi divisível {c} vezes.')
if c == 2:       # se o contador, que é o número de vezes que ele foi divisível for até 2, então é primo
    print('E por isso ele não é primo.')
else:
    print('E por isso ele não é primo.')
