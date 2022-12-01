'''Faça um programa que leia o idade e sexo de várias pessoas
assim que o usuário cadastrar uma pessoa, o programa pergunte
se ele quer continuar. Ao final mostre:
Quantas pessoas tem mais de 18 anos;
quantos são homens
quantas mulheres tem menos de 20
'''

idade = cmulher = chomem = cidade = 0

print('Cadastramento')
                    #Input de dados e repetição
while True:
    print('*' * 20)
    print('CADASTRE UMA PESSOA')
    print('*' * 20)
    idade = int(input('IDADE: '))
                #Contador da idade
    if idade > 18:
        cidade = cidade + 1
                #Contador do sexo
    s = ' '
    while s not in 'MF':
        s = str(input('Sexo [M/F]:')).strip().upper()[0]
        if s == 'M':
            chomem = chomem + 1
    if idade < 20 and s == 'F':
        cmulher = cmulher + 1
                #Continuar ou não
    tipo = ' '
    while tipo not in 'SN':
        tipo = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if tipo == 'N':
        break
print(f'{cidade} pessoas tem mais de 18, {chomem} são homens e tem {cmulher} mulher com menos de 20 anos.')