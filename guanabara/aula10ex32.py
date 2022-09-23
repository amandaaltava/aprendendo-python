'''Faça um programa que leia um ano qualquer e mostre se ele é ano BISSEXTO'''

from datetime import date

ano = int(input('Digite um ano e te direi se é ou não ano bissexto ou coloque 0 para analisar o ano atual:'))
if ano== 0:
    ano == date.today().year    #today() é a funçao e year é o parametro que se quer da data atual da máquina
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:         # condições, a ordem deve seguir os cálculos matemáticos socialmente aceitos
    print('O ano {} é ano Bissexto.' .format(ano))
else:
    print('O ano {} não é ano bissexto.' .format(ano))
