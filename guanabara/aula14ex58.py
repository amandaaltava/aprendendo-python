from random import randint
from time import sleep



'''print('----' * 20)
print('Adivinhe pequeno gafanhoto, qual é o número que estou pensando.')
print('----' * 20)

contador = 1
num1 = randint(0, 11)
num = float(input('Digite o número de seu palpite de 0 à 10: '))

while num1 != num:
    print('\033[1;31mProcessando\033[m')
    sleep(1)
    num = float(input(f'\033[1;97mErrou, que burrx dá zero para elx, tenta outra vez:\033[m'))
    contador = contador + 1

    if num == num1:
        print(f'\033[1;31mAcertou!\033[m Eu pensei em {num1}. foram necessárias {contador} tentativas para acertar.\033[m')
        break

print('fim')'''

#
#
#
# from random import randint
# from time import sleep
#
#
#
# print('----' * 20)
# print('Adivinhe pequeno gafanhoto, qual é o número que estou pensando.')
# print('----' * 20)
#
# contador = 1
# num1 = randint(0, 11)
#
# print(num1)
# num = float(input('Digite o número de seu palpite de 0 à 10: '))
#
# print('\033[1;31mProcessando\033[m')
# sleep(1)
#
# while num!=num1:
#     contador = contador + 1
#     print(f'\033[1;97mErrou, que burrx dá zero para elx, tenta outra vez.\033[m')
#     num = float(input('Tenta outro: '))
#
# print(f'\033[1;31mAcertou!\033m Eu pensei em {num1}. foram necessárias {contador} tentativas para acertar.')
#
#

computador = randint(0,10)
acertou = False
palpites = 0

print('Pensei num número de 0 a 10, advinha')

while not acertou:    #enquanto certou nao for true
    jogador = int(input('Qual seu palpite?: '))
    palpites +=1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:  #confere se o número está acima ou abaixo do esperado
            print('Mais, outra vez:')
        elif jogador > computador:
            print('Menos, outra vez:')
print(f'Acertou com {palpites} tentativas. Joguei {computador}')