'''Faça um programa que  leia o ano de nascimento de sete pessoas
e no final mostre quantas pessoas atingiram a maturidade, 21 anos
e quantas não atingiram ainda a maturidade'''
from datetime import date

maior = 0 # inicia o somador da maioridade
menor = 0 # inicia o somador da menor idade
for laco in range(0, 7):              # laço
    ano = int(input(f'Em que ano a pessoa {laco +1}º nasceu?: '))
    ano = date.today().year - ano  # calculo da maioridade
    if ano >= 21:    # condição para maioridade
        maior = maior + 1
    else:        # condição para a menor idado
        menor = menor + 1

print(f'{maior} pessoas atingiram a maioridade.')
print(f'{menor} pessoas não atingiram a maioridade.')
