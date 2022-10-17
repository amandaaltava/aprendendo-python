'''Programa que peça o sexo da pessoa e fique pedindo até que ela digite corretamente.'''

sexo = ''
while sexo != 'F':
    sexo = str(input('Olá, por favor digite o sexo, sendo M ou F.: ')).strip().upper()[0]
    if sexo == 'F':
        print('Você digitou corretamente.')
    elif sexo == 'M':
        print('Você digitou corretamente.')
        exit()

    else:
        print('Ah não! Você não digitou corretamente, digite outra vez..')

print('Vamos seguir...')