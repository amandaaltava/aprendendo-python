'''Faça um programa que receba 3 retas e diga se é um triangulo:
 equilatero de todos lados iguais
 isoceles dois lados iguais
 escaleno todos lados diferentes'''

r1 = float(input('Insira a medida de uma reta: '))
r2 = float(input('Insira a medida de outra reta: '))
r3 = float(input('Insira a medida da última reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Pode formar um triângulo.')
    if r1 == r2 and r2 == r3:
        print('Esse é um triângulo equilatero.')
    elif r1 != r2 and r2 != r3 and r1 != r3:
        print('escaleno.')
    else:
        print('Esse triâgulo é isóceles.')
else:
    print('Não pode formar um triângulo.')
