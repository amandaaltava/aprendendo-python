cores = {'limpa': '\033[m',
          'verde':'\033[34m',
         'pretoebranco':'\033[7;40m'}

n1 = int(input('digite um valor: '))
n2 = int(input('digite um outro valor:'))
s = n1 + n2
print('A soma entre {}{}{} e {}{}{} vale {}{}{}'.format(cores['verde'], n1, cores['limpa'], cores['verde'], n2, cores['limpa'], cores['pretoebranco'], s, cores['limpa']))
