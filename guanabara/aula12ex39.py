'''Faça um programa que leia o NAO  de nascimento de um jovem e informe se acordo com a sua idade:
- se ele ainda vai se alistar
- se é a hora de se alistar
- se já passou do tempo do alistamento
- se falta ou se passou do tempo seu programa também deve mostrar'''
from datetime import date

ano = int(input('\033[1;97mDigite a seu ano de nascimento: \033[m'))
sexo = str(input('Qual é o seu sexo, feminino [F] ou masculino [M]: ')).strip() .upper()
idade = date.today().year - ano

if sexo == ('F'):
    print('Você não precisa se alistar.')
elif idade < 18:
    print(f'Você ainda vai se alistar, faltam {18 - idade} anos, isso acontecerá no ano de {date.today().year + (18 - idade)} ')
elif idade > 18:
    print(f'Você já passou {idade - 18} anos do prazo de se alistar, você deveria ter se alistado no ano de {date.today().year - (idade - 18)} ')
elif idade == 18:
    print(f'Você tem {idade} anos, em {date.today().year} já é hora de você se alistar.')
