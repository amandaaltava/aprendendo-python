n = int(input('Please, insert a number: '))

print('O número antecessor de {}{}{} é {}{}{} e o seu sucessor é {}{}{}' .format('\033[32m', n, '\033[m', '\033[31m', n-1, '\033[m', '\033[32m', n+1, '\033[m'))
