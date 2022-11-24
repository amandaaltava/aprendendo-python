'''Faça um programa que mostre a tabuada de vários números, um de cada vez,
para cada valor digitado pelo usuário. O programa será interrompido quando
o número solicitado for negativo.'''

n = c = 0    # inicia as variáveis

while True:     #looping infinito para automatizar o input
    n = int(input('Digite um número te darei a tabuada dele:'))
    if n < 0:      #condição e parada
        break
    print('--' * 20)
    for c in range(0, 10):     #laço para imprimir a tabuada de 1 a 10
        c = c +1
        print(f'{n} x {c} = {n*c} ')

    print('--' * 20)
print('Acabou, fim.')