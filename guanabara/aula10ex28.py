'''nome = str(input('Qual é o seu nome: '))
if nome == 'Amanda':
    print('Que nome lindo')
else:
    print('Seu nome é besta')
print('Bom dia {}' .format(nome))'''


'''n1 = float(input('Digite a caralha da sua primeira nota: '))
n2 = float(input('Digite a merda da sua segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi {:.1f}.' .format(m))
if m >= 6.0:
    print('Sua média está meia boca')
else:
    print('Sua média está uma mérdia seu merdia')'''


'''Faça um programa que pense num número e pergunte ao usuário qual foi o número que ele pensou, e escreva na tela se ele acertou ou errou o número'''

from random import randint #importa a função randint da biblioteca random
from time import sleep #importa a função sleep da biblioteca time

print('**' * 30)  #imprime a graça na tela.
print('Estou pensando em um número de 0 a 5, adivinhe qual número é')
print('**' * 30)
num = float(input('Qual foi o número que eu pensei?: ')) #o usuário digita o número que imagina.
num1 = randint(0,5)  #sorteia o número no intervalo de 0 a 5.
print('PROCESSANDO...')
sleep(2) #faz o pc "adormecer por uns instantes - escolhidos, e então aparece o restante do programa.
if num == num1:
    print('Eu pensei em {}. Parabéns, vc acertou!' .format(num1))
else:
    print('Eu pensei em {}. YOU LOOOSE'.format(num1))
print('Better luck next time! Try Again!')
