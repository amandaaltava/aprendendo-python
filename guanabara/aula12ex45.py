'''Faça um programa que jogue jokên pô'''
from random import randint
from time import sleep

# apresentação
print('+++++' * 10)
print('Vamos jogar joken po')
print(('+++++' *10))

# recebe numero do jogador
jogador = int(input('Escolha: [0] pedra [1] papel [2] tesoura: '))

# conferindo se o número digitado é válido
if jogador != 0 and jogador != 1 and jogador != 2:
    print('\033[1;31;40mNão seja idiota, jogue direito!\033[m')
    exit()

# arrumando os itens numa lista
itens = ('Pedra', 'Papel', 'Tesoura')

# sorteando o número do computador
pc = randint(0, 2)

# exibe a mensagem do resultado
print('**' * 10)
print(f'O COMPUTADOR JOGOU {(itens[pc])}.')
print(f'VOCÊ JOGOU {(itens[jogador])}')
print('**' * 10)

sleep(1)

# comparando com a jogada do pc
if jogador == pc:
    print('\033[1;34mEMPATE!\033[m')
elif jogador == 0 and pc == 2:
    print('\033[1;32mVocê venceu!\033[m')
elif jogador == 1 and pc == 0:
    print('\033[1;32mVocê Venceu!\033[m')
elif jogador == 2 and pc == 1:
    print('\033[1;31mVocê venceu!\033[m')
else:
    print('\033[1;31mComputador venceu!\033[m')
