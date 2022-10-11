'''Faça um programq que leia o primeiro termo e
a razão de uma PROGRESSAO ARITIMÉTICA
 no final mostre os 10 PRIMEIROS TERMOS dessa progressao

 obs: pulando de tantos em tantos'''

pt = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
decimo = pt + (10 - 1) * r    # calculo do nonagéssimo elemento da pa
for c in range(pt, decimo + r, r):
    print(f'{c}', end='>')
print('Acabou')




