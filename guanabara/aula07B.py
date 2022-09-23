n = int(input('Insert a number: '))


print('Você inseriu o número {}{}{}, e o seu dobro é {}{}{}, seu triplo é {}{}{} e sua raiz quadrada é {}{}{}'
      .format('\033[7;40m', n, '\033[m', '\033[7;41m', n*2, '\033[m', '\033[7;30;42m', n*3, '\033[m', '\033[7;43m', n**(1/2), '\033[m'))



