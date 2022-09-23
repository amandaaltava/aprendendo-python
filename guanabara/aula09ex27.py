'''Faça um programa que leia o nome completo de uma pessoa, mostrando
em seguida o primeiro e último nome separadamente'''

nome = str(input('Insira seu nome completo:')).strip()
nome1 = nome.split()
nome2 = str(nome1[0])
print('Seu primeiro nome é: {} ' .format(nome2))
print('Seu último nome é: {} ' .format(nome1[len(nome1)-1]))
