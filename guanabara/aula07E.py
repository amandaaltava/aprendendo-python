from time import sleep
print('**-' * 11)
n = int(input('insira um número inteiro: '))
print('**-' * 11)
print(f'A tabuada de \033[1;32m{n}\033[m é: ')
print('--' * 10)
sleep(1)
print(f'\033[34m{n} x {1}\033[m = \033[32m{n*1}\033[m')
print(f'\033[34m{n} x {2}\033[m = \033[32m{n*2}\033[m')
print(f'\033[34m{n} x {3}\033[m = \033[32m{n*3}\033[m')
print(f'\033[34m{n} x {4}\033[m = \033[32m{n*4}\033[m')
print(f'\033[34m{n} x {5}\033[m = \033[32m{n*5}\033[m')
print(f'\033[34m{n} x {6}\033[m = \033[32m{n*6}\033[m')
print(f'\033[34m{n} x {7}\033[m = \033[32m{n*7}\033[m')
print(f'\033[34m{n} x {8}\033[m = \033[32m{n*8}\033[m')
print(f'\033[34m{n} x {9}\033[m = \033[32m{n*9}\033[m')
print(f'\033[34m{n} x {10}\033[m = \033[32m{n*10}\033[m')


