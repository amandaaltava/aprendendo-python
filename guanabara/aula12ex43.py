'''Faça um programa que leia a altura e peso de uma pessoa e calcule seu imc e mostre
de acordo com a tabela:
abaixo de 18.5 abaixo do peso
entre 18.5 e 25 peso ideal
25 até 30 sobrepeso
30 ate 40 obeside
acima de 40 obesidade morbidade'''

# pede os dados em tela
peso = float(input('Digite seu peso: '))
altura = float(input('Digite ca sua altura: '))

# calcula o imc e printa
imc = peso / (altura**2)
print(f'Seu IMC é {imc:.2f}')

# teste de imc e print
if imc < 18.5:
    print('E vc está Abaixo do peso.')
elif 18.5 <= imc < 25:
    print('E vc está no Peso Ideal.')
elif 25 <= imc < 30:
    print('E vc está com Sobrepeso.')
elif 30 <= imc < 40:
    print('E vc está com Obesidade.')
elif imc >= 40:
    print('E vc está com Obesidade mórbida.')
