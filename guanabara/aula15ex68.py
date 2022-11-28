'''Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER,
mostrando o total de vitorias consecutivas que ele
conquistou no final do jogo'''
from random import randint
n = 0
cont = 0
pc = 0
escolha = ' '
resultado = 0
conta = 0
soma = 0
resultado2 = ' '


print('=-' * 20)
print('Par ou Ímpar, escolha e boa sorte. Vai precisar!!')
print('=-' * 20)
                #Impõe a condição até ser interrompida
while True:
                #Input dos dados do jogador
    n = int(input('Escolha um número de 0 a 10: '))
    escolha = input('Escolha PAR ou ÍMPAR [P/I]: ').upper(). strip()[0]

                #Escolha do Pc
    pc = randint(0, 10)
    print(f'O computador jogou {pc}')
                #Soma para saber se é par
    soma = n + pc
    print(f'Resultado {soma}')
                #Conta para saber se é par, divisão com resto
    conta = soma % 2
    #print(f'Resto {conta}')

                #Condição de vencedor
    if conta == 0:
        resultado = 'P'
        resultado2 = 'PAR'
        if resultado == escolha:
            cont = cont + 1
        else:
            print('Você perdeu!')
            break

    elif conta == 1:
        resultado = 'I'
        resultado2 = 'ÍMPAR'
        if resultado == escolha:
            cont = cont + 1
        else:
            print('Você perdeu!')
            break
    print(f'Você jogou {n} e o Pc jogou {pc}. Total de {soma} deu {resultado2}')

print('_' * 20)
print(f'Você jogou {n} e o Pc jogou {pc}. Total de {soma} deu {resultado2}')
print(f'Game Over, você venceu {cont} vezes..')


 '''Código do guanabara

v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}.', end='')
    print('Deu PAR' if total % 2 == 0 else 'Deu ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v = v + 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER!! Você venceu {v} vezes.')

'''