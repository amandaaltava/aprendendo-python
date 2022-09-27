'''Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício
indo de 10 até 0 com uma pausa de 1 segundo entre eles

ps vai usar o sleep e mostrar um emoji de fogos de artifício - buscar
biblioteca de emoticons'''
from time import sleep

# cria o laço de repetição com nome de C
for c in range(10, -1, -1): # conta de 10 a zero -1 de trás para frente, ao contrário)
    print(c)
    sleep(1)

print('Bum dum tssss')
