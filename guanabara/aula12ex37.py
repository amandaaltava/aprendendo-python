'''Faça um programa que leia um numero inteiro e converta em binario, hexadecimal ou octal'''

numero = int(input('Insira um número \033[1;30minteiro\033[m: '))
opcao = int(input('Escolha em qual modo quer converter: 1 - binario 2 hexadecimal 3 octal: '))

if opcao == 1:
    print(f'O número {numero} em binário é {bin(numero)[2:]} .') # os colchetes com o [2;] indica que deve começar a exibir a partir do 3 caracter, escondendo assim o identificador e a letra resultantes da conversão pelo comando
elif opcao == 2:
    print(f'O número {numero} em hexadecimal é {hex(numero)[2:]} .')
elif opcao == 3:
    print(f'O número {numero} em octal é {oct(numero)[2:]} .')
else:
    print('Não seja burro, escolha UMA das TRÊS OPÇÕES!')


