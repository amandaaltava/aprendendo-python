'''Jogo de par ou impar que só para quando  o jogador perder
deve mostrar o numero consecutivos de vitórias'''

from random import randint


pc = 0
jogador = 0
escolha = 0
cont = 0
comparador = 0

print('+-' * 10)
print('Vamos jogar par ou ímpar, o jogo acaba quando você perder. Boa sorte! Vai precisar.')
print('-+' * 10)
                   #Input do jogador e escolha de par ou ímpar
while True:
    jogador = int(input('Digite um número: '))
    escolha = str(input('Quer Ímpar ou Par? [I - P]: ')).upper().strip()
                   #Escolha do pc
    pc = randint(0, 11)
    print(pc)
                    #Condição para vencer
    if jogador %  = 0:
        comparador = P
    else:
        comparador = I

    if comparador == escolha:
        cont = cont + 1
        print('Deu win')
    else:
        break

print(f'Você venceu {cont} vezes.')