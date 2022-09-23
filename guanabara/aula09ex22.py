#Tem várias soluções CORRETAS

'''Crie um programa que leia o nome completo de uma pesso e mostre:
- o nome com todas as letras maiúsculas
- o nome com todas minúsculas
- quantas letras tem ao todo
- quantas letras tem o primeiro nome '''

'''nome = str(input('Insira seu nome completo: '))
print('Seu nome em letras maiúsculas é: {}' .format(nome.upper()))
print('Seu nome em letras minúsuclas é: {}' .format(nome.lower()))
print('Seu nome completo possui {} letras' .format(len(nome)))
firstnome = nome.split()
print('Seu primeiro nome tem {} letras' .format(len(firstnome[0])))'''

'''nome = str(input('Digite seu nome completo: '))
print('Seu nome em maiúsculas é: {}'.format(nome.upper()))
print('Seu nome em minúsculas é: {}'.format(nome.lower()))
print('Seu nome possui {} letras'.format(len(nome.replace(' ', ''))))
dividido = nome.split()
print('{} possui {} letras'.format(dividido[0], len(dividido[0])))'''

'''nome = str(input('Digite o seu nome completo: '))
print('Seu nome em maior: {} ' .format(nome.upper()))
print('Seu nome em menor: {} ' .format(nome.lower()))
print('Seu nome tem {} letras.' .format(len(nome) - nome.count(' ')))'''

nome = str(input('Digite seu nome completo: ')).strip() #o strip aqui já elimina os espaços nas pontas já agora no início da função
print('Seu nome em maiusculas é: \033[31m{} \033[m'.format(nome.upper()))
print('Seu nome em minúsculas é: {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras. '.format(len(nome) - nome.count(' ')))




