'''Faça um programa que leia o comprimento de três retas
e diga ao usuário se é possivel criar ou nao um triângulo com elas.'''

a = float(input('\033[4;32mDigite um dos lados: '))
b = float(input('\033[4;34mDigite um outro lado: '))
c = float(input('\033[4;33mDigite o último lado: '))

if a < b + c and b < a + c and c < a + b:
    print('\033[1;32;41mÉ UM TRIANGULO')
else:
    print('\033[1;30;41mNão é um TRIÂNGULO')
