'''Refaça o exercicio 009 mostrando a
 tabuada do numero escolhido pelo usuário
 só que agora utilizando o faço fór'''

# pede o número escolhido
numero = int(input('Insira o número que vc quer a tabuada: '))

# seta o contador
contador = 0

print(f'A sua tabuada do {numero} é:')

# calcula o intervalo
for tab in range(1, 11):
    multi = numero * tab         # faz o calculo
    contador = contador +1       # inicia o contador
    print(f'{numero} x {contador} = {multi}')
