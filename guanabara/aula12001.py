nome = str(input('Qual é o seu nome? '))
if nome == 'Trouxa':
    print(f'Que nome comum \033[1;34m{nome}\033[m. ')
elif nome == 'Idiota' or nome == 'Imbecil' or nome == 'Retardado':
    print(f'Seu nome é bem magavilhoso, \033[33m{nome}\033[m')
else:
    print('Seu nome é bem bosta.')
print(f'Vai se fuder \033[1;31m{nome}\033[m')
