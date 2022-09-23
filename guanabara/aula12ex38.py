'''Faça um progama que leia dois numero inteiro e os compare, mostrando na tela a mensagem:
- o primeiro valor é maior
- o segundo valor é maior
- não existe valor maior, os dois são iguais'''
# recebe os valores do usuário
Primeiro = int(input('\033[1;30;107mDigite um número inteiro: \033[m'))
Segundo = int(input('\033[7;30;107mDigite outro número inteiro: \033[m'))

# condicional para comparar
if Primeiro > Segundo:
    print(f'\033[97;41mO Primeiro valor é o Maior.\033[m')
elif Segundo > Primeiro:
    print(f'\033[1;34mO Segundo valor é o Maior. \033[m')
elif Primeiro == Segundo:
    print('\033[1;97;41mNão existe valor Maior, os dois são iguais. \033[m')


