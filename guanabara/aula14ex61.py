'''Faça um programq que leia o primeiro termo e
a razão de uma PROGRESSAO ARITIMÉTICA
 no final mostre os 10 PRIMEIROS TERMOS dessa progressao

 obs: pulando de tantos em tantos'''

pt = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
termo = pt
cont = 1

while cont <=10:
    print(f' {termo} >  ', end = '')
    termo = termo + r
    cont += 1

print('End')