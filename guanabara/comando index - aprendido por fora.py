'''Faça um progama que leia uma frase pelo teclado e mostre:
quantas x aparece a letra A
em qual posição ela aparece pela primeira x
em qual posição ela aparece pela última x'''

'''nome = str(input('Insira uma frase aqui: ')) .lower() .strip()
nome1 = str(nome.replace('à', 'a'))
nome2 = str(nome1.replace('â', 'a'))
nome3 = str(nome2.replace('á', 'a'))
nome4 = str(nome3.replace('ã', 'a')).upper() .split()
nome5 = str(' '.join(nome4))
nome6 = str(nome5.count('A'))
print('A letra A, aparece {} vezes. '.format(nome6))
nome7 = str(nome5.index('A')+1)
print('A letra A aparece pela primeira vez na posição {}' . format(nome7))
print('A letra A aparece por último na posição {} ' .format(nome5.rindex('A')+1))

#o index procura do começo SEMPRE, vc pode mandar começar pela esquerda como padrão, sem nada, apenas o comando index
#ou usar o R e L para alterar, esquerda ou direita para INICIAR'''

frase = 'Curso em Video Python'
print(frase.index('o')+1)

