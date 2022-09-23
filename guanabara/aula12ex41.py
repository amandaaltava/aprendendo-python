'''Faça um programa que leia o ano de nascimento sw um atleta e mostre sua categoria, de acordo com a idade:
- ate 9 mirim
- ate 14 infantil
- ate 19 anos junior
- ate 20 senior
- acima master'''
from datetime import date

ano = int(input('Digite o ano de nascimento:'))
idade = date.today().year - ano

if idade <= 9:
    print(f'Vc tem {idade} e sua categoria é MIRIM.')
elif idade <= 14:
    print(f'Vc tem {idade} e sua categoria é Infantil. ')
elif idade <= 19:
    print(f'Sua idade é {idade} e sua categoria é Junior. ')
elif idade <= 25:
    print(f'Sua idade é {idade} categoria é senior.')
else:
    print(f'Sua idade é {idade} e sua categoria é MASTER.')



