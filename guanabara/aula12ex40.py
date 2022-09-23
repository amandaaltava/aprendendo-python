'''Faça um programa que leia duas notas e calule sua média mostrando uma mensagem
no final de acordo com a média
- abaixo de 5.0 reprovado
- entre 5.0 e 6.9 recuperação
- igual ou acima de 7.00 APROVADO.'''

n1 = float(input('Digitea a sua nota: '))
n2 = float(input('Digite sua nota: '))
media = n1 + n2 / 2

# verifica qual é a classificação
if media <= 4.99:
    print('Reprovado')
elif media >= 5.0 and media <= 6.9:
    print('recuperação')
elif media >= 7.0:
    print('aprovado')
