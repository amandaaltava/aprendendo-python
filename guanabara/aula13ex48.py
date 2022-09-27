'''Faça um programa que calcule a soma entre todos os
números ímpares que são múltiplos de 3 e que
se encontram no intervalo de 1 até 500

ps: divisível por 3
'''

# inicia o contador
cont = 0

# inicia o somador
soma = 0

for c in range(1, 501, 2):           # seta o laço pulando 1 numero, ou seja, pula do 1 para o 3
   if c % 3 == 0:                 # coloca a condição, se o laço estiver com um número que seja múltiplo de 3.
       cont = cont + 1            # declara que o contador recebe ele e soma 1.
       soma += c                  # seta que o somador recebe ele mesmo e o valor do laço

print(f'O total de multiplos foi {cont} e a soma é {soma}.')
