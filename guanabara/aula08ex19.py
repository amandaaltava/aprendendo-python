import random
a1 = input('Insira o nome do primeiro alune:')
a2 = input('Insira o nome do segundo alune:')
a3 = input('Insira o nome do terceiro alune:')
a4 = input('Insira o nome do quarto alune:')
lista = [ a1 , a2 , a3 , a4 ]
print('O aluno sorteado é {}' .format(random.choice(lista )))


