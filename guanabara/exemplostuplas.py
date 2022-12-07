lanche = ('hamburguer', 'suco', 'pizza', 'pudim' , 'batata frita')
# print(lanche[-3:])

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}') #---- desse jeito ele mostra o índice(com o len)

# for pos, comida in enumerate(lanche):
#    print(f'Eu vou comer {comida} na posição {pos}')

# for comida in lanche:
#   print(f'Eu vou comer {comida}')


#print(sorted(lanche)) #---- sorted é em ordem, ele só vai imprimir em uma LISTA por ordem alfabética, a tupla continua imutável como na linha print abaixo
#print(lanche)

'''a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c.count(5))'''



'''a = ( 2, 5, 4 )
b = ( 5, 8, 1, 2 )
c = a + b
print( c.index( 5 ) )'''