'''Faça um programa que pergunte ao funcionario o seu salário
e calcule o valor de seu aumento
para salários superiores a R$ 1250 um aumento de 10%
para salaários inferiores ou iguais, um aumento de 15%'''

salario = float(input('Digite seu salário R$ '))
if salario > 1250:
    print('Seu salário é R${:.2f}, seu aumento é de R${:.2f} e o total será de R${:.2f}.' .format(salario, salario * 0.10, (salario * 0.10 +salario)))  # a conta pode ser também  s * 10 / 100
else:
    print('Seu salário é R${:.2f}, seu aumento é de R${:.2f} e o total será de R${:.2f}.' .format(salario, salario * 0.15, (salario * 0.15 + salario)))   # a conta pode ser também s * 15 /100
