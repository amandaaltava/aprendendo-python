'''Faça um programa que mostre na tela todos os números pares que estão
no intervalo entre 1 e 50'''

for c in range(0, 51, 2):
   # print('.') se eu colocar esse pontinho para imprimir, ele vai marcar quantas vezes o laço teve que fazer a iteração
   # se eu coloco como iteração (o último número no parenteses do laço) como 1, ele vai calcular todas, de 1 em 1, se eu coloco
   # a ordem para ele ir de 2 em 2 ele só vai testar a iteração a cada 2 casas, e isso economiza processamento.
    print(c, end=' ')


