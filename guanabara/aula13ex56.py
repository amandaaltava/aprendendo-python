'''Desenvolva um programa que leia o
nome, idade e sexo de 4 pessoas
no final do programa mostre:
- a media de idade do grupo
qual é o nome do homem mais velho
quantas mulheres tem menos de 20 anos.'''
import statistics
from statistics import mean
'''
cont1 = 0
nomeM = 0

for laco in range(1, 5):
    nome = str(input(f'Digite o nome da {laco}º pessoa: ').upper())
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite F ou M para FEMININO ou MASCULINO: ').upper())

if sexo == 'F' and idade < 21:
    cont1 = cont1

if sexo == 'M':
    nomeM = max(idade)

idadeM = statistics.mean(idade)

print(f'O homem mais velho se chama {nomeM}.')
print(f'A média de idade do grupo é {idadeM}.')
print(f'{cont1} mulheres tem menos de 21 anos.')'''

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0

for p in range(1, 5):
    print(f'...{p}°...')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]:')).strip()
    somaidade = somaidade + idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 = totmulher20 + 1


mediaidade = somaidade / 4
print(f'A média de idade do grupo é de {mediaidade} anos.')
print(f'O homem  mais velho se chama {nomevelho}, e tem {maioridadehomem} anos.')
print(f'Ao todo são {totmulher20} mulheres com menos de 20 anos.')
